from email.mime import message
import json
import os


# =========================================================
# LOAD CROP DATABASE
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CROPS_FILE = os.path.join(
    BASE_DIR,
    "database",
    "crops.json"
)

with open(CROPS_FILE, "r", encoding="utf-8") as f:
    CROP_DATA = json.load(f)


# =========================================================
# FARMER ASSISTANT CHATBOT
# =========================================================

def process_question(message):

    message = message.lower().strip()

    print("CHATBOT MESSAGE:", message)

    greetings = [
        "hello",
        "hi",
        "hey",
        "হ্যালো",
        "হাই",
        "আসসালামু আলাইকুম"
    ]

    if message in greetings:

        return {
            "type": "general",
            "reply": (
                "আসসালামু আলাইকুম! 👋 "
                "আমি Farmer Assistant। "
                "আপনার কৃষি, মাছ চাষ, Biofloc, আবহাওয়া "
                "বা খামার সম্পর্কিত প্রশ্ন করতে পারেন।"
            )
        }
    # ==============================
    # FISH INFORMATION
    # ==============================
    fish_recommendation_keywords = [
        "fish",
        "মাছ",
       "fish information",
       "মাছ চাষ পদ্ধতি কিভাবে করব?",
       "মাছ চাষ",
       "fish recommendation system",
       "fish recommendation"
        
    ]

    if any(word in message for word in fish_recommendation_keywords):

        return {
            "type": "fish",
            "reply": " মাছ চাষ সম্পর্কিত তথ্যের জন্য আমাদের fish recommendation system দেখতে পারেন।",
            "link": "/aquaculture",
            "link_text": " Fish recommendation system দেখুন →"
        }

    # =====================================================
    # CROP DETECTION
    # =====================================================

    detected_crop = None
    detected_crop_info = None

    for crop_key, crop_info in CROP_DATA.items():

        if (
            crop_key.lower() in message
            or crop_info["name"].lower() in message
            or crop_info["bangla_name"] in message
        ):
            detected_crop = crop_key
            detected_crop_info = crop_info
            break


    # =====================================================
    # CROP QUESTION
    # =====================================================

    if detected_crop:

        # -------------------------------------------------
        # TEMPERATURE
        # -------------------------------------------------

        if any(word in message for word in [
            "তাপমাত্রা",
            "গরম",
            "ঠান্ডা",
            "temperature",
            "degree",
            "ডিগ্রি"
        ]):
            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🌡️ উপযুক্ত তাপমাত্রা: "
                    f"{detected_crop_info['growing_conditions']['temperature']}"
                )
            }

            # -------------------------------------------------
            # Soil
            # -------------------------------------------------

        if any(word in message for word in [
            "মাটি",
            "soil",
            "জমি"
        ]):

           return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🌱 উপযুক্ত মাটি: "
                    f"{detected_crop_info['growing_conditions']['soil']}"
                )
           }


        # -------------------------------------------------
        # Water
        # -------------------------------------------------

        if any(word in message for word in [
            "পানি",
            "জল",
            "সেচ",
            "water",
            "irrigation"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"💧 পানি ও সেচ: "
                    f"{detected_crop_info['growing_conditions']['water_requirement']}"
                )
            }


        # -------------------------------------------------
        # Humidity
        # -------------------------------------------------

        if any(word in message for word in [
            "আর্দ্রতা",
            "আর্দ্র",
            "humidity"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🌦️ উপযুক্ত আর্দ্রতা: "
                    f"{detected_crop_info['growing_conditions']['humidity']}"
                )
            }


        # -------------------------------------------------
        # Season
        # -------------------------------------------------

        if any(word in message for word in [
            "মৌসুম",
            "সময়",
            "সময়",
            "কখন",
            "season",
            "চাষের সময়",
            "চাষের সময়"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"📅 উপযুক্ত মৌসুম: "
                    f"{detected_crop_info['growing_conditions']['season']}"
                )
            }


        # -------------------------------------------------
        # Fertilizer
        # -------------------------------------------------

        if any(word in message for word in [
            "সার",
            "সারের",
            "fertilizer"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🧪 সার: "
                    f"{detected_crop_info['farming']['fertilizer']}"
                )
            }


        # -------------------------------------------------
        # Cultivation
        # -------------------------------------------------

        if any(word in message for word in [
            "চাষ",
            "চাষাবাদ",
            "চাষ পদ্ধতি",
            "cultivation",
            "কিভাবে চাষ",
            "কীভাবে চাষ"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🌱 চাষ পদ্ধতি: "
                    f"{detected_crop_info['farming']['cultivation']}"
                )
            }

        # -------------------------------------------------
        # Harvest
        # -------------------------------------------------

        if any(word in message for word in [
            "সংগ্রহ",
            "কাটা",
            "কখন কাটব",
            "কখন কাটবো",
            "harvest"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🌾 সংগ্রহ: "
                    f"{detected_crop_info['harvest']['harvest']}\n"
                    f"⏱️ সময়কাল: "
                    f"{detected_crop_info['harvest']['duration']}"
                )
            }
        # -------------------------------------------------
        # SEED REQUIREMENT
        # -------------------------------------------------

        if any(word in message for word in [
            "বীজ",
            "বীজের পরিমাণ",
            "কত বীজ",
            "seed",
            "seed requirement"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🌱 বীজের প্রয়োজন: "
                    f"{detected_crop_info['farming']['seed_requirement']}"
                )
            }
        # -------------------------------------------------
        # IRRIGATION
        # -------------------------------------------------

        if any(word in message for word in [
            "সেচ",
            "সেচ ব্যবস্থা",
            "কতবার সেচ",
            "irrigation",
            "পানি দিতে"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"💧 সেচ ব্যবস্থাপনা: "
                    f"{detected_crop_info['farming']['irrigation']}"
                )
            }
        # -------------------------------------------------
        # DISEASE
        # -------------------------------------------------

        if any(word in message for word in [
            "রোগ",
            "রোগবালাই",
            "disease",
            "রোগ কী",
            "রোগগুলো"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🦠 সাধারণ রোগ: "
                    f"{detected_crop_info['protection']['common_diseases']}"
                )
            }
        # -------------------------------------------------
        # PEST
        # -------------------------------------------------

        if any(word in message for word in [
            "পোকা",
            "পোকামাকড়",
            "পোকামাকড়",
            "pest",
            "insect"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"🐛 সাধারণ পোকামাকড়: "
                    f"{detected_crop_info['protection']['common_pests']}"
                )
            }
        # -------------------------------------------------
        # DURATION
        # -------------------------------------------------

        if any(word in message for word in [
            "কতদিন",
            "কত দিন",
            "সময়কাল",
            "সময়কাল",
            "কত দিনে",
            "কতদিনে",
            "duration"
        ]):

            return {
                "type": "crop",
                "reply": (
                    f"🌾 {detected_crop_info['bangla_name']} "
                    f"({detected_crop_info['name']})\n\n"
                    f"⏱️ চাষের সময়কাল: "
                    f"{detected_crop_info['harvest']['duration']}"
                )
            }

        # -------------------------------------------------
        # ONLY CROP NAME
        # -------------------------------------------------

        return {
            "type": "crop",
            "reply": (
                f"🌾 {detected_crop_info['bangla_name']} "
                f"({detected_crop_info['name']})\n\n"

                f"🌱 মাটি: "
                f"{detected_crop_info['growing_conditions']['soil']}\n"

                f"🌡️ তাপমাত্রা: "
                f"{detected_crop_info['growing_conditions']['temperature']}\n"

                f"💧 পানি: "
                f"{detected_crop_info['growing_conditions']['water_requirement']}\n"

                f"🌦️ আর্দ্রতা: "
                f"{detected_crop_info['growing_conditions']['humidity']}\n"

                f"📅 মৌসুম: "
                f"{detected_crop_info['growing_conditions']['season']}\n"

                f"🧪 সার: "
                f"{detected_crop_info['farming']['fertilizer']}\n"

                f"🌱 চাষ পদ্ধতি: "
                f"{detected_crop_info['farming']['cultivation']}\n"

                f"🌾 সংগ্রহ: "
                f"{detected_crop_info['harvest']['harvest']}\n"

                f"⏱️ সময়কাল: "
                f"{detected_crop_info['harvest']['duration']}"
            )
        }


    # =====================================================
    # CROP GENERAL KEYWORDS
    # =====================================================

    crop_recommendation_keywords = [
        "crop recommendation",
        "ফসল সুপারিশ",
        "ফসল",
        "crop",
        "আমার জমিতে কোন ফসল রোপণ করব?",
        "জমিতে ফসল রোপণ"
    ]

    if any(word in message for word in crop_recommendation_keywords):

        return {
            "type": " crop recommendation",
            "reply": " জমিতে ফসল রোপণ সম্পর্কিত তথ্যের জন্য আমাদের crop recommendation system দেখতে পারেন।",
            "link": "/crop-recommendation",
            "link_text": " crop recommendation দেখুন →"
        }


    # =====================================================
    # POND / FISH
    # =====================================================

    fish_keywords = [
        "hatchery",
        "হ্যাচারি",   
    ]

    if any(word in message for word in fish_keywords):

        return {
            "type": "fish",
            "reply": " মাছ হ্যাচারি সম্পর্কিত তথ্যের জন্য আমাদের Fish Fish hatchery section দেখতে পারেন।",
            "link": "/fish-information",
            "link_text": " Fish hatchery দেখুন →"
        }

    live_stock_keywords = [
        "livestock",
        "জীবপ্রাণ",
        "পশু",
        "গবাদি",
        "গবাদি পশু",
        "domestic animals",
        "গৃহপালিত পশু",
        "গবাদিপশু কিভাবে পালন করব?"
    ]
    if any(word in message for word in live_stock_keywords):

        return {
            "type": "livestock",
            "reply": "গবাদি পশু সম্পর্কিত তথ্যের জন্য আমাদের Livestock section দেখতে পারেন।",
            "link": "/live-stock",
            "link_text": " Livestock information দেখুন →"
        }

    # BIOFLOC
    biofloc_keywords = [
        "biofloc",
        "বায়োফ্লক",
        "বায়ো",
        "ফ্লক"
    ]

    if any(word in message for word in biofloc_keywords):

        return {
            "type": "biofloc",
            "reply": "  Biofloc সম্পর্কিত তথ্য দেখতে নিচের বাটনে ক্লিক করুন।",
            "link": "/biofloc",
            "link_text": "  Biofloc recommendation দেখুন"
        }

    biofloc_keywords = [
        "ras",
        "পানি পুনঃব্যবহারভিত্তিক মাছ চাষ পদ্ধতি",
        "Recirculating Aquaculture System",
        "নিয়ন্ত্রিত পরিবেশে মাছ চাষ পদ্ধতি",
        "নিয়ন্ত্রিত পরিবেশে মাছ চাষ কিভাবে করব?"
        
    ]

    if any(word in message for word in biofloc_keywords):

        return {
            "type": "ras",
            "reply": "  RAS পদ্ধতিতে মাছ চাষ সম্পর্কিত তথ্য দেখতে নিচের বাটনে ক্লিক করুন।",
            "link": "/ras",
            "link_text": "  RAS recommendation দেখুন"
        }
    cageculture_keywords = [
        "cage culture",
        "গুটি চাষ",
        "খাঁচা সংস্কৃতি মাছ চাষ পদ্ধতি",
        "খাঁচা পদ্ধতিতে মাছ চাষ কিভাবে করব?",
        "cage"   
    ]

    if any(word in message for word in cageculture_keywords):

        return {
            "type": "cageculture",
            "reply": "  Cage Culture পদ্ধতিতে মাছ চাষ সম্পর্কিত তথ্য দেখতে নিচের বাটনে ক্লিক করুন।",
            "link": "/cage-culture",
            "link_text": "  Cage Culture recommendation দেখুন"
        }
    marineculture_keywords = [
        "marine culture",
        "মার্জিন কালচার",
        "সমুদ্র সংস্কৃতি মাছ চাষ পদ্ধতি",
        "সমুদ্র পদ্ধতিতে মাছ চাষ কিভাবে করব?",
        "marine",
        "সমুদ্রতে কিভাবে মাছ চাষ করব?",
        "marin",
        "marin culture"
    ]

    if any(word in message for word in marineculture_keywords):

        return {
            "type": "marinculture",
            "reply": "  Marine Culture পদ্ধতিতে মাছ চাষ সম্পর্কিত তথ্য দেখতে নিচের বাটনে ক্লিক করুন।",
            "link": "/marine-culture",
            "link_text": "  Marine Culture recommendation দেখুন"
        }



    # WEATHER
    weather_keywords = [
        "weather",
        "আবহাওয়া",
        "বৃষ্টি",
        "তাপমাত্রা",
        "temperature"
    ]

    if any(word in message for word in weather_keywords):

        return {
            "type": "weather",
            "reply": " আবহাওয়া সম্পর্কিত তথ্য দেখতে নিচের বাটনে ক্লিক করুন।",
            "link": "/weather-info",
            "link_text": " Weather Information দেখুন"
        }


    # =====================================================
    # MARKET
    # =====================================================

    marketprice_keywords = [
        "market",
        "market price",
        "market rate",
        "বাজার",
        "দাম",
        "বাজারদর",
    ]

    if any(word in message for word in marketprice_keywords):

        return {
            "type": "market_price",
            "reply": " বাজারদর দেখতে নিচের বাটনে ক্লিক করুন।",
            "link": "/market-price",
            "link_text": " Market Price দেখুন"
        }

    # =====================================================
    # DEFAULT
    # =====================================================

    return {
        "type": "general",
        "reply": (
            "দুঃখিত, এই বিষয়ে আমার agriculture database-এ "
            "তথ্য নেই।"
        )
    }