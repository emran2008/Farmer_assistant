def detect_intent(message):

    message = message.lower()

    biofloc_keywords = [
        "biofloc",
        "বায়োফ্লক",
        "বায়োফ্লক",
        "ammonia",
        "অ্যামোনিয়া",
        "nitrite",
        "নাইট্রাইট",
        "alkalinity",
        "alkalinity",
        "tank",
        "ট্যাংক"
    ]

    if any(word in message for word in biofloc_keywords):
        return "biofloc"

    return "general"