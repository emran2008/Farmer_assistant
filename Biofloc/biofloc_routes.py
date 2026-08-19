from flask import Blueprint, render_template, request, jsonify

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

        # এখন শুধু test response
        return jsonify({
            "success": True,
            "reply": f"আপনার প্রশ্ন পেয়েছি: {message}"
        })

    except Exception as e:

        return jsonify({
            "success": False,
            "reply": f"Server error: {str(e)}"
        }), 500