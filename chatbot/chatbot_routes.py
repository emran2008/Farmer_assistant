from flask import Blueprint, render_template, request, jsonify

from .chatbot import process_question


chatbot_bp = Blueprint("chatbot", __name__)


@chatbot_bp.route("/chatbot")
def chatbot_page():

    return render_template("chatbot.html")


@chatbot_bp.route("/api/chatbot", methods=["POST"])
def chatbot_api():

    try:

        data = request.get_json(silent=True) or {}

        message = data.get("message", "").strip()

        if not message:

            return jsonify({
                "success": False,
                "reply": "দয়া করে একটি প্রশ্ন লিখুন।"
            })

        result = process_question(message)

        return jsonify({
            "success": True,
            "type": result.get("type", "general"),
            "reply": result.get("reply", ""),
            "link": result.get("link"),
            "link_text": result.get("link_text")
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "reply": "দুঃখিত, একটি সমস্যা হয়েছে।",
            "error": str(e)
        })