def analyze_biofloc(
    temperature,
    ph,
    do_value,
    ammonia,
    nitrite,
    biofloc,
    length,
    width,
    depth,
    fish_count,
    feed
):
    """
    Biofloc water quality and basic system analysis.
    """

    # -------------------------
    # BASIC CALCULATIONS
    # -------------------------

    volume = length * width * depth

    density = fish_count / volume if volume > 0 else 0

    floc_amount = volume * biofloc


    # -------------------------
    # PROBLEMS
    # -------------------------

    problems = []

    if do_value < 5:
        problems.append("DO কম")

    if ph < 6.5 or ph > 8:
        problems.append("pH আদর্শ নয়")

    if ammonia > 0.05:
        problems.append("Ammonia বেশি")

    if nitrite > 0.5:
        problems.append("Nitrite বেশি")


    # -------------------------
    # CONDITION
    # -------------------------

    if len(problems) == 0:
        condition = "Biofloc-এর অবস্থা ভালো"
    else:
        condition = "মনোযোগ প্রয়োজন"


    # -------------------------
    # ADVICE
    # -------------------------

    advice = []

    if do_value < 5:
        advice.append(
            "DO কম — Aerator পর্যাপ্তভাবে চালু রাখুন এবং পানিতে অক্সিজেন নিশ্চিত করুন।"
        )
    else:
        advice.append(
            "DO বর্তমানে ভালো আছে — Aeration নিয়মিত পর্যবেক্ষণ করুন।"
        )

    if ph < 6.5 or ph > 8:
        advice.append(
            "pH আদর্শ সীমার বাইরে — ধীরে ধীরে pH সমন্বয় করুন।"
        )
    else:
        advice.append(
            "pH বর্তমানে গ্রহণযোগ্য সীমায় আছে।"
        )

    if ammonia > 0.05:
        advice.append(
            "Ammonia বেশি — Feed কমানো, Aeration বৃদ্ধি এবং Biofloc-এর ভারসাম্য পরীক্ষা করুন।"
        )

    if nitrite > 0.5:
        advice.append(
            "Nitrite বেশি — পানির গুণমান পরীক্ষা করুন এবং Biofloc system-এর microbial balance বজায় রাখুন।"
        )

    advice.append(
        "প্রতিদিন Temperature, pH, DO, Ammonia ও Nitrite পরীক্ষা করুন।"
    )

    advice.append(
        "মাছের biomass অনুযায়ী Feed দিন এবং অতিরিক্ত খাবার দেওয়া এড়িয়ে চলুন।"
    )

    advice.append(
        "Biofloc-এর ঘনত্ব নিয়মিত পর্যবেক্ষণ করুন।"
    )


    # -------------------------
    # RETURN RESULT
    # -------------------------

    return {
        "temperature": temperature,
        "ph": ph,
        "do": do_value,
        "ammonia": ammonia,
        "nitrite": nitrite,
        "biofloc": biofloc,

        "volume": volume,
        "density": density,
        "fish_count": fish_count,
        "feed": feed,
        "floc_amount": floc_amount,

        "problems": problems,
        "condition": condition,
        "advice": advice
    }