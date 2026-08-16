/* =========================================================
   FISH MARKET SYSTEM
   Bangladesh Division → District → Upazila
========================================================= */


/* =========================================================
   LOCATION DATA
========================================================= */

const LOCATION_DATA = {

    "চট্টগ্রাম": {

        "চট্টগ্রাম": [
            "আনোয়ারা",
            "বাঁশখালী",
            "বোয়ালখালী",
            "চন্দনাইশ",
            "ফটিকছড়ি",
            "হাটহাজারী",
            "কর্ণফুলী",
            "লোহাগাড়া",
            "মীরসরাই",
            "পটিয়া",
            "রাঙ্গুনিয়া",
            "রাউজান",
            "সন্দ্বীপ",
            "সাতকানিয়া",
            "সীতাকুণ্ড"
        ],

        "কক্সবাজার": [
            "কক্সবাজার সদর",
            "চকরিয়া",
            "ঈদগাঁও",
            "কুতুবদিয়া",
            "মহেশখালী",
            "পেকুয়া",
            "রামু",
            "টেকনাফ",
            "উখিয়া"
        ],

        "কুমিল্লা": [
            "আদর্শ সদর",
            "সদর দক্ষিণ",
            "বুড়িচং",
            "ব্রাহ্মণপাড়া",
            "চান্দিনা",
            "চৌদ্দগ্রাম",
            "দাউদকান্দি",
            "দেবিদ্বার",
            "হোমনা",
            "লাকসাম",
            "লালমাই",
            "মেঘনা",
            "মনোহরগঞ্জ",
            "মুরাদনগর",
            "নাঙ্গলকোট",
            "তিতাস",
            "বরুড়া"
        ],

        "ফেনী": [
            "ফেনী সদর",
            "ছাগলনাইয়া",
            "দাগনভূঞা",
            "পরশুরাম",
            "ফুলগাজী",
            "সোনাগাজী"
        ],

        "নোয়াখালী": [
            "বেগমগঞ্জ",
            "চাটখিল",
            "কোম্পানীগঞ্জ",
            "হাতিয়া",
            "কবিরহাট",
            "সেনবাগ",
            "সুবর্ণচর",
            "নোয়াখালী সদর",
            "সোনাইমুড়ী"
        ],

        "লক্ষ্মীপুর": [
            "কমলনগর",
            "রামগতি",
            "রামগঞ্জ",
            "রায়পুর",
            "লক্ষ্মীপুর সদর"
        ],

        "চাঁদপুর": [
            "চাঁদপুর সদর",
            "ফরিদগঞ্জ",
            "হাজীগঞ্জ",
            "হাইমচর",
            "কচুয়া",
            "মতলব উত্তর",
            "মতলব দক্ষিণ",
            "শাহরাস্তি"
        ],

        "ব্রাহ্মণবাড়িয়া": [
            "আখাউড়া",
            "আশুগঞ্জ",
            "বিজয়নগর",
            "ব্রাহ্মণবাড়িয়া সদর",
            "বাঞ্ছারামপুর",
            "কসবা",
            "নবীনগর",
            "নাসিরনগর",
            "সরাইল"
        ],

        "রাঙ্গামাটি": [
            "রাঙ্গামাটি সদর",
            "বাঘাইছড়ি",
            "বরকল",
            "বিলাইছড়ি",
            "জুরাছড়ি",
            "লংগদু",
            "নানিয়ারচর",
            "রাজস্থলী",
            "কাউখালী",
            "কাপ্তাই"
        ],

        "খাগড়াছড়ি": [
            "খাগড়াছড়ি সদর",
            "দীঘিনালা",
            "পানছড়ি",
            "মাটিরাঙ্গা",
            "মহালছড়ি",
            "মানিকছড়ি",
            "রামগড়",
            "লক্ষ্মীছড়ি",
            "গুইমারা"
        ],

        "বান্দরবান": [
            "বান্দরবান সদর",
            "আলীকদম",
            "থানচি",
            "রুমা",
            "লামা",
            "নাইক্ষ্যংছড়ি",
            "রোয়াংছড়ি"
        ]

    },


    "ঢাকা": {

        "ঢাকা": [
            "ধামরাই",
            "দোহার",
            "কেরানীগঞ্জ",
            "নবাবগঞ্জ",
            "সাভার"
        ],

        "গাজীপুর": [
            "কালীগঞ্জ",
            "কালিয়াকৈর",
            "কাপাসিয়া",
            "শ্রীপুর",
            "গাজীপুর সদর"
        ],

        "নারায়ণগঞ্জ": [
            "আড়াইহাজার",
            "বন্দর",
            "রূপগঞ্জ",
            "সোনারগাঁ",
            "নারায়ণগঞ্জ সদর"
        ],

        "নরসিংদী": [
            "বেলাব",
            "মনোহরদী",
            "নরসিংদী সদর",
            "পলাশ",
            "রায়পুরা",
            "শিবপুর"
        ],

        "মুন্সীগঞ্জ": [
            "গজারিয়া",
            "লৌহজং",
            "মুন্সীগঞ্জ সদর",
            "সিরাজদিখান",
            "শ্রীনগর",
            "টঙ্গীবাড়ী"
        ],

        "মানিকগঞ্জ": [
            "দৌলতপুর",
            "ঘিওর",
            "হরিরামপুর",
            "মানিকগঞ্জ সদর",
            "সাটুরিয়া",
            "শিবালয়",
            "সিংগাইর"
        ],

        "টাঙ্গাইল": [
            "বাসাইল",
            "ভূঞাপুর",
            "দেলদুয়ার",
            "ধনবাড়ী",
            "ঘাটাইল",
            "গোপালপুর",
            "মধুপুর",
            "মির্জাপুর",
            "নাগরপুর",
            "সখীপুর",
            "টাঙ্গাইল সদর",
            "কালিহাতী"
        ],

        "কিশোরগঞ্জ": [
            "অষ্টগ্রাম",
            "বাজিতপুর",
            "ভৈরব",
            "হোসেনপুর",
            "ইটনা",
            "করিমগঞ্জ",
            "কটিয়াদী",
            "কুলিয়ারচর",
            "মিঠামইন",
            "নিকলী",
            "পাকুন্দিয়া",
            "কিশোরগঞ্জ সদর",
            "তাড়াইল"
        ],

        "ফরিদপুর": [
            "আলফাডাঙ্গা",
            "ভাঙ্গা",
            "বোয়ালমারী",
            "চরভদ্রাসন",
            "ফরিদপুর সদর",
            "মধুখালী",
            "নগরকান্দা",
            "সদরপুর",
            "সালথা"
        ],

        "গোপালগঞ্জ": [
            "গোপালগঞ্জ সদর",
            "কাশিয়ানী",
            "কোটালীপাড়া",
            "মুকসুদপুর",
            "টুঙ্গিপাড়া"
        ],

        "মাদারীপুর": [
            "কালকিনি",
            "মাদারীপুর সদর",
            "রাজৈর",
            "শিবচর",
            "ডাসার"
        ],

        "শরীয়তপুর": [
            "ভেদরগঞ্জ",
            "ডামুড্যা",
            "গোসাইরহাট",
            "জাজিরা",
            "নড়িয়া",
            "শরীয়তপুর সদর"
        ],

        "রাজবাড়ী": [
            "বালিয়াকান্দি",
            "গোয়ালন্দ",
            "কালুখালী",
            "পাংশা",
            "রাজবাড়ী সদর"
        ]

    },


    "ময়মনসিংহ": {

        "ময়মনসিংহ": [
            "ময়মনসিংহ সদর",
            "ত্রিশাল",
            "ভালুকা",
            "মুক্তাগাছা",
            "ফুলবাড়ীয়া",
            "গফরগাঁও",
            "গৌরীপুর",
            "ঈশ্বরগঞ্জ",
            "নান্দাইল",
            "ধোবাউড়া",
            "ফুলপুর",
            "হালুয়াঘাট",
            "তারাকান্দা"
        ],

        "জামালপুর": [
            "জামালপুর সদর",
            "বকশীগঞ্জ",
            "দেওয়ানগঞ্জ",
            "ইসলামপুর",
            "মাদারগঞ্জ",
            "মেলান্দহ",
            "সরিষাবাড়ী"
        ],

        "নেত্রকোণা": [
            "নেত্রকোণা সদর",
            "আটপাড়া",
            "বারহাট্টা",
            "দুর্গাপুর",
            "কলমাকান্দা",
            "কেন্দুয়া",
            "খালিয়াজুরী",
            "মদন",
            "মোহনগঞ্জ",
            "পূর্বধলা"
        ],

        "শেরপুর": [
            "শেরপুর সদর",
            "ঝিনাইগাতী",
            "নকলা",
            "নালিতাবাড়ী",
            "শ্রীবরদী"
        ]

    },


    "রংপুর": {

        "রংপুর": [
            "বদরগঞ্জ",
            "কাউনিয়া",
            "গঙ্গাচড়া",
            "মিঠাপুকুর",
            "পীরগাছা",
            "পীরগঞ্জ",
            "রংপুর সদর",
            "তারাগঞ্জ"
        ],

        "দিনাজপুর": [
            "বিরামপুর",
            "বিরল",
            "বোচাগঞ্জ",
            "চিরিরবন্দর",
            "ফুলবাড়ী",
            "ঘোড়াঘাট",
            "হাকিমপুর",
            "কাহারোল",
            "খানসামা",
            "নবাবগঞ্জ",
            "পার্বতীপুর",
            "দিনাজপুর সদর",
            "বীরগঞ্জ"
        ],

        "গাইবান্ধা": [
            "ফুলছড়ি",
            "গাইবান্ধা সদর",
            "গোবিন্দগঞ্জ",
            "পলাশবাড়ী",
            "সাদুল্লাপুর",
            "সুন্দরগঞ্জ",
            "সাঘাটা"
        ],

        "নীলফামারী": [
            "ডোমার",
            "ডিমলা",
            "জলঢাকা",
            "কিশোরগঞ্জ",
            "নীলফামারী সদর",
            "সৈয়দপুর"
        ],

        "কুড়িগ্রাম": [
            "ভূরুঙ্গামারী",
            "চর রাজিবপুর",
            "চিলমারী",
            "ফুলবাড়ী",
            "কুড়িগ্রাম সদর",
            "নাগেশ্বরী",
            "রাজারহাট",
            "রৌমারী",
            "উলিপুর"
        ],

        "লালমনিরহাট": [
            "আদিতমারী",
            "হাতীবান্ধা",
            "কালীগঞ্জ",
            "লালমনিরহাট সদর",
            "পাটগ্রাম"
        ],

        "ঠাকুরগাঁও": [
            "বালিয়াডাঙ্গী",
            "হরিপুর",
            "পীরগঞ্জ",
            "রানীশংকৈল",
            "ঠাকুরগাঁও সদর"
        ],

        "পঞ্চগড়": [
            "আটোয়ারী",
            "বোদা",
            "দেবীগঞ্জ",
            "পঞ্চগড় সদর",
            "তেঁতুলিয়া"
        ]

    },


    "সিলেট": {

        "সিলেট": [
            "বালাগঞ্জ",
            "বিয়ানীবাজার",
            "বিশ্বনাথ",
            "কোম্পানীগঞ্জ",
            "ফেঞ্চুগঞ্জ",
            "গোলাপগঞ্জ",
            "গোয়াইনঘাট",
            "জৈন্তাপুর",
            "কানাইঘাট",
            "সিলেট সদর",
            "জকিগঞ্জ",
            "দক্ষিণ সুরমা",
            "ওসমানীনগর"
        ],

        "মৌলভীবাজার": [
            "বড়লেখা",
            "জুড়ী",
            "কমলগঞ্জ",
            "কুলাউড়া",
            "মৌলভীবাজার সদর",
            "রাজনগর",
            "শ্রীমঙ্গল"
        ],

        "হবিগঞ্জ": [
            "আজমিরীগঞ্জ",
            "বাহুবল",
            "বানিয়াচং",
            "চুনারুঘাট",
            "হবিগঞ্জ সদর",
            "লাখাই",
            "মাধবপুর",
            "নবীগঞ্জ",
            "শায়েস্তাগঞ্জ"
        ],

        "সুনামগঞ্জ": [
            "ছাতক",
            "দিরাই",
            "ধর্মপাশা",
            "দোয়ারাবাজার",
            "জগন্নাথপুর",
            "জামালগঞ্জ",
            "শান্তিগঞ্জ",
            "সুনামগঞ্জ সদর",
            "তাহিরপুর",
            "মধ্যনগর",
            "শাল্লা"
        ]

    },


    "খুলনা": {

        "খুলনা": [
            "বটিয়াঘাটা",
            "দাকোপ",
            "ডুমুরিয়া",
            "দিঘলিয়া",
            "কয়রা",
            "পাইকগাছা",
            "ফুলতলা",
            "রূপসা",
            "তেরখাদা"
        ],

        "বাগেরহাট": [
            "বাগেরহাট সদর",
            "চিতলমারী",
            "ফকিরহাট",
            "কচুয়া",
            "মোল্লাহাট",
            "মোংলা",
            "মোড়েলগঞ্জ",
            "রামপাল",
            "শরণখোলা"
        ],

        "সাতক্ষীরা": [
            "আশাশুনি",
            "কলারোয়া",
            "কালীগঞ্জ",
            "সাতক্ষীরা সদর",
            "শ্যামনগর",
            "তালা",
            "দেবহাটা"
        ],

        "যশোর": [
            "অভয়নগর",
            "বাঘারপাড়া",
            "চৌগাছা",
            "ঝিকরগাছা",
            "কেশবপুর",
            "মণিরামপুর",
            "শার্শা",
            "যশোর সদর"
        ],

        "ঝিনাইদহ": [
            "হরিণাকুন্ডু",
            "ঝিনাইদহ সদর",
            "কালীগঞ্জ",
            "কোটচাঁদপুর",
            "মহেশপুর",
            "শৈলকুপা"
        ],

        "মাগুরা": [
            "মাগুরা সদর",
            "মহম্মদপুর",
            "শালিখা",
            "শ্রীপুর"
        ],

        "নড়াইল": [
            "কালিয়া",
            "লোহাগড়া",
            "নড়াইল সদর"
        ],

        "কুষ্টিয়া": [
            "ভেড়ামারা",
            "দৌলতপুর",
            "খোকসা",
            "কুমারখালী",
            "কুষ্টিয়া সদর",
            "মিরপুর"
        ],

        "চুয়াডাঙ্গা": [
            "আলমডাঙ্গা",
            "চুয়াডাঙ্গা সদর",
            "দামুড়হুদা",
            "জীবননগর"
        ],

        "মেহেরপুর": [
            "গাংনী",
            "মেহেরপুর সদর",
            "মুজিবনগর"
        ]

    },


    "বরিশাল": {

        "বরিশাল": [
            "আগৈলঝাড়া",
            "বাবুগঞ্জ",
            "বাকেরগঞ্জ",
            "বানারীপাড়া",
            "গৌরনদী",
            "হিজলা",
            "মেহেন্দিগঞ্জ",
            "মুলাদী",
            "উজিরপুর",
            "বরিশাল সদর"
        ],

        "ভোলা": [
            "ভোলা সদর",
            "বোরহানউদ্দিন",
            "চরফ্যাশন",
            "দৌলতখান",
            "লালমোহন",
            "মনপুরা",
            "তজুমদ্দিন"
        ],

        "ঝালকাঠি": [
            "ঝালকাঠি সদর",
            "কাঠালিয়া",
            "নলছিটি",
            "রাজাপুর"
        ],

        "পটুয়াখালী": [
            "বাউফল",
            "দশমিনা",
            "দুমকি",
            "কলাপাড়া",
            "মির্জাগঞ্জ",
            "পটুয়াখালী সদর",
            "রাঙ্গাবালী",
            "গলাচিপা"
        ],

        "পিরোজপুর": [
            "ভান্ডারিয়া",
            "কাউখালী",
            "মঠবাড়িয়া",
            "নাজিরপুর",
            "নেছারাবাদ",
            "পিরোজপুর সদর",
            "ইন্দুরকানী"
        ],

        "বরগুনা": [
            "আমতলী",
            "বামনা",
            "বরগুনা সদর",
            "বেতাগী",
            "পাথরঘাটা",
            "তালতলী"
        ]

    },


    "রাজশাহী": {

        "রাজশাহী": [
            "বাগমারা",
            "চারঘাট",
            "দুর্গাপুর",
            "গোদাগাড়ী",
            "মোহনপুর",
            "পবা",
            "পুঠিয়া",
            "তানোর",
            "বাঘা"
        ],

        "বগুড়া": [
            "আদমদীঘি",
            "বগুড়া সদর",
            "ধুনট",
            "দুপচাঁচিয়া",
            "গাবতলী",
            "কাহালু",
            "নন্দীগ্রাম",
            "সারিয়াকান্দি",
            "শাজাহানপুর",
            "শেরপুর",
            "শিবগঞ্জ",
            "সোনাতলা"
        ],

        "জয়পুরহাট": [
            "আক্কেলপুর",
            "ক্ষেতলাল",
            "কালাই",
            "পাঁচবিবি",
            "জয়পুরহাট সদর"
        ],

        "নওগাঁ": [
            "আত্রাই",
            "বদলগাছী",
            "ধামইরহাট",
            "মান্দা",
            "মহাদেবপুর",
            "নওগাঁ সদর",
            "নিয়ামতপুর",
            "পত্নীতলা",
            "পোরশা",
            "রানীনগর",
            "সাপাহার"
        ],

        "নাটোর": [
            "বাগাতিপাড়া",
            "বড়াইগ্রাম",
            "গুরুদাসপুর",
            "লালপুর",
            "নলডাঙ্গা",
            "নাটোর সদর",
            "সিংড়া"
        ],

        "চাঁপাইনবাবগঞ্জ": [
            "ভোলাহাট",
            "গোমস্তাপুর",
            "নাচোল",
            "শিবগঞ্জ",
            "চাঁপাইনবাবগঞ্জ সদর"
        ],

        "পাবনা": [
            "আটঘরিয়া",
            "বেড়া",
            "ভাঙ্গুড়া",
            "চাটমোহর",
            "ফরিদপুর",
            "ঈশ্বরদী",
            "পাবনা সদর",
            "সাঁথিয়া",
            "সুজানগর"
        ],

        "সিরাজগঞ্জ": [
            "বেলকুচি",
            "চৌহালী",
            "কামারখন্দ",
            "কাজীপুর",
            "রায়গঞ্জ",
            "শাহজাদপুর",
            "সিরাজগঞ্জ সদর",
            "তাড়াশ",
            "উল্লাপাড়া"
        ]

    }

};


/* =========================================================
   FISH LIST
========================================================= */

const FISH_LIST = [

    "রুই",
    "কাতলা",
    "মৃগেল",
    "তেলাপিয়া",
    "পাঙ্গাস",
    "শিং",
    "মাগুর",
    "কৈ",
    "পাবদা",
    "বোয়াল",
    "চিংড়ি",
    "গলদা চিংড়ি"

];



/* =========================================================
   OFFICIAL SOURCES
========================================================= */

const OFFICIAL_SOURCES = [

    {
        name:"মৎস্য অধিদপ্তর",
        description:"মৎস্য চাষ, মৎস্য সম্পদ ও সরকারি মৎস্য সেবা",
        url:"https://fisheries.gov.bd/"
    },

    {
        name:"প্রাণিসম্পদ অধিদপ্তর",
        description:"প্রাণিসম্পদ ও পশুপাখি সংক্রান্ত সরকারি সেবা",
        url:"https://dls.gov.bd/"
    },

    {
        name:"বাংলাদেশ মৎস্য উন্নয়ন কর্পোরেশন (BFDC)",
        description:"মৎস্য অবতরণ, সংরক্ষণ, প্রক্রিয়াজাতকরণ ও বাজারজাতকরণ",
        url:"https://bfdc.gov.bd/"
    },

    {
        name:"মৎস্য ও প্রাণিসম্পদ তথ্য দপ্তর",
        description:"মৎস্য ও প্রাণিসম্পদ সংক্রান্ত সরকারি তথ্য",
        url:"https://flid.gov.bd/"
    },

    {
        name:"মৎস্য ও প্রাণিসম্পদ মন্ত্রণালয়",
        description:"মন্ত্রণালয়ের সরকারি তথ্য ও সেবা",
        url:"https://mofl.gov.bd/"
    },

    {
        name:"DLS e-Trade Portal",
        description:"প্রাণিসম্পদ খাতের অনলাইন সেবা",
        url:"https://etrade.dls.gov.bd/"
    }

];



/* =========================================================
   SAMPLE HATCHERY DATA
========================================================= */

const HATCHERIES = [

    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"ঢাকা",
        district:"রাজবাড়ী",
        upazila:"রাজবাড়ী সদর",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া",
            "পাঙ্গাস"
        ],

        phone:"01700-000000",

        email:"info@fisheries.gov.bd"
    },


    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"ঢাকা",
        district:"মাদারীপুর",
        upazila:"মাদারীপুর সদর",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া",
            "পাঙ্গাস"
        ],

        phone:"01700-000001",

        email:"info@fisheries.gov.bd"
    },


    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"ঢাকা",
        district:"মানিকগঞ্জ",
        upazila:"মানিকগঞ্জ সদর",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া"
        ],

        phone:"01700-000002",

        email:"info@fisheries.gov.bd"
    },


    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"ময়মনসিংহ",
        district:"ময়মনসিংহ",
        upazila:"ময়মনসিংহ সদর",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া",
            "পাঙ্গাস",
            "শিং",
            "মাগুর"
        ],

        phone:"01700-000003",

        email:"info@fisheries.gov.bd"
    },


    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"রংপুর",
        district:"রংপুর",
        upazila:"রংপুর সদর",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া",
            "পাঙ্গাস"
        ],

        phone:"01700-000004",

        email:"info@fisheries.gov.bd"
    },


    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"চট্টগ্রাম",
        district:"চট্টগ্রাম",
        upazila:"মীরসরাই",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া",
            "পাঙ্গাস"
        ],

        phone:"01700-000005",

        email:"info@fisheries.gov.bd"
    },


    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"চট্টগ্রাম",
        district:"কুমিল্লা",
        upazila:"বুড়িচং",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া",
            "পাঙ্গাস"
        ],

        phone:"01700-000006",

        email:"info@fisheries.gov.bd"
    },


    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"খুলনা",
        district:"ঝিনাইদহ",
        upazila:"কোটচাঁদপুর",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া",
            "পাঙ্গাস",
            "শিং",
            "মাগুর"
        ],

        phone:"01700-000007",

        email:"info@fisheries.gov.bd"
    },


    {
        name:"মৎস্য বীজ উৎপাদন খামার",
        division:"সিলেট",
        district:"সুনামগঞ্জ",
        upazila:"শান্তিগঞ্জ",

        fish:[
            "রুই",
            "কাতলা",
            "মৃগেল",
            "তেলাপিয়া"
        ],

        phone:"01700-000008",

        email:"info@fisheries.gov.bd"
    }

];



/* =========================================================
   DOM
========================================================= */

const division = document.getElementById("division");

const district = document.getElementById("district");

const upazila = document.getElementById("upazila");

const fish = document.getElementById("fish");

const service = document.getElementById("service");

const searchBtn = document.getElementById("searchBtn");

const results = document.getElementById("results");

const locationStatus =
    document.getElementById("locationStatus");

const officialSources =
    document.getElementById("officialSources");

const orderModal =
    document.getElementById("orderModal");

const closeModal =
    document.getElementById("closeModal");

const orderForm =
    document.getElementById("orderForm");

const sellerInfo =
    document.getElementById("sellerInfo");



/* =========================================================
   LOAD DIVISIONS
========================================================= */

Object.keys(LOCATION_DATA).forEach(
    function(divisionName){

        const option =
            document.createElement("option");

        option.value =
            divisionName;

        option.textContent =
            divisionName;

        division.appendChild(option);

    }
);



/* =========================================================
   LOAD FISH
========================================================= */

FISH_LIST.forEach(
    function(fishName){

        const option =
            document.createElement("option");

        option.value =
            fishName;

        option.textContent =
            fishName;

        fish.appendChild(option);

    }
);



/* =========================================================
   LOAD OFFICIAL SOURCES
========================================================= */

OFFICIAL_SOURCES.forEach(
    function(source){

        officialSources.innerHTML += `

            <div class="source-card">

                <h3>
                    🏛️ ${source.name}
                </h3>

                <p>
                    ${source.description}
                </p>

                <a
                    href="${source.url}"
                    target="_blank"
                    rel="noopener noreferrer">

                    অফিসিয়াল ওয়েবসাইট খুলুন ↗

                </a>

            </div>

        `;

    }
);



/* =========================================================
   DIVISION CHANGE
========================================================= */

division.addEventListener(
    "change",
    function(){

        district.innerHTML = `
            <option value="">
                জেলা নির্বাচন করুন
            </option>
        `;

        upazila.innerHTML = `
            <option value="">
                প্রথমে জেলা নির্বাচন করুন
            </option>
        `;

        district.disabled = true;

        upazila.disabled = true;


        if(!division.value){

            locationStatus.textContent =
                "📍 প্রথমে বিভাগ নির্বাচন করুন";

            return;

        }


        const districts =
            LOCATION_DATA[division.value];


        Object.keys(districts).forEach(
            function(districtName){

                const option =
                    document.createElement("option");

                option.value =
                    districtName;

                option.textContent =
                    districtName;

                district.appendChild(option);

            }
        );


        district.disabled = false;


        locationStatus.textContent =
            "✅ এখন জেলা নির্বাচন করুন";

    }
);



/* =========================================================
   DISTRICT CHANGE
========================================================= */

district.addEventListener(
    "change",
    function(){

        upazila.innerHTML = `
            <option value="">
                উপজেলা নির্বাচন করুন
            </option>
        `;

        upazila.disabled = true;


        if(!district.value){

            return;

        }


        const upazilas =
            LOCATION_DATA
            [division.value]
            [district.value];


        upazilas.forEach(
            function(upazilaName){

                const option =
                    document.createElement("option");

                option.value =
                    upazilaName;

                option.textContent =
                    upazilaName;

                upazila.appendChild(option);

            }
        );


        upazila.disabled = false;


        locationStatus.textContent =
            "✅ এখন উপজেলা নির্বাচন করুন";

    }
);



/* =========================================================
   UPAZILA CHANGE
========================================================= */

upazila.addEventListener(
    "change",
    function(){

        if(!upazila.value){

            return;

        }


        locationStatus.textContent =

            `✅ ${division.value}
             → ${district.value}
             → ${upazila.value}`;

    }
);



/* =========================================================
   SEARCH
========================================================= */

searchBtn.addEventListener(
    "click",
    function(){

        if(
            !division.value ||
            !district.value ||
            !upazila.value ||
            !fish.value
        ){

            results.innerHTML = `

                <div class="result-card">

                    <div class="result-header">

                        <h3>
                            ⚠️ তথ্য অসম্পূর্ণ
                        </h3>

                        <p>
                            বিভাগ, জেলা, উপজেলা এবং মাছ নির্বাচন করুন।
                        </p>

                    </div>

                </div>

            `;

            return;

        }


        const matched =
            HATCHERIES.filter(
                function(h){

                    return (

                        h.division === division.value &&

                        h.district === district.value &&

                        h.upazila === upazila.value &&

                        h.fish.includes(fish.value)

                    );

                }
            );


        if(service.value === "buy"){

            showBuyResults(matched);

        }else{

            showHatcheryResults(matched);

        }

    }
);



/* =========================================================
   HATCHERY RESULTS
========================================================= */

function showHatcheryResults(data){

    if(data.length === 0){

        results.innerHTML = `

            <div class="result-card">

                <div class="result-header">

                    <h3>
                        🔎 হ্যাচারি পাওয়া যায়নি
                    </h3>

                    <p>
                        ${division.value}
                        →
                        ${district.value}
                        →
                        ${upazila.value}
                    </p>

                </div>

                <p>
                    নির্বাচিত এলাকার জন্য বর্তমানে
                    সংযুক্ত হ্যাচারি তালিকায় তথ্য নেই।
                </p>

            </div>

        `;

        return;

    }


    results.innerHTML = `

        <div class="result-card">

            <div class="result-header">

                <h3>
                    ✅ ${data.length} টি হ্যাচারি পাওয়া গেছে
                </h3>

                <p>
                    ${division.value}
                    →
                    ${district.value}
                    →
                    ${upazila.value}
                    |
                    🐟 ${fish.value}
                </p>

            </div>


            <div class="seller-grid">

                ${data.map(
                    createSellerCard
                ).join("")}

            </div>

        </div>

    `;

}



/* =========================================================
   BUY RESULTS
========================================================= */

function showBuyResults(data){

    if(data.length === 0){

        results.innerHTML = `

            <div class="result-card">

                <div class="result-header">

                    <h3>
                        🛒 বিক্রেতা পাওয়া যায়নি
                    </h3>

                    <p>
                        এই এলাকার জন্য বর্তমানে
                        সংযুক্ত বিক্রেতা/হ্যাচারি নেই।
                    </p>

                </div>

                <p>
                    অন্য উপজেলা নির্বাচন করে আবার চেষ্টা করুন।
                </p>

            </div>

        `;

        return;

    }


    results.innerHTML = `

        <div class="result-card">

            <div class="result-header">

                <h3>
                    🛒 মাছ / পোনা কিনুন
                </h3>

                <p>
                    ${division.value}
                    →
                    ${district.value}
                    →
                    ${upazila.value}
                </p>

            </div>


            <div class="seller-grid">

                ${data.map(
                    createBuyCard
                ).join("")}

            </div>

        </div>

    `;

}



/* =========================================================
   SELLER CARD
========================================================= */

function createSellerCard(h){

    return `

        <div class="seller-card">

            <h3>
                🏭 ${h.name}
            </h3>

            <div class="seller-row">
                📍 ${h.district},
                ${h.upazila}
            </div>

            <div class="seller-row">
                🐟 ${h.fish.join(", ")}
            </div>

            <div class="seller-row">
                📞 ${h.phone}
            </div>

            <div class="seller-row">
                ✉️ ${h.email}
            </div>

        </div>

    `;

}



/* =========================================================
   BUY CARD
========================================================= */

function createBuyCard(h,index){

    return `

        <div class="seller-card">

            <h3>
                🐟 ${h.name}
            </h3>

            <div class="seller-row">
                📍 ${h.district},
                ${h.upazila}
            </div>

            <div class="seller-row">
                🐟 ${h.fish.join(", ")}
            </div>

            <div class="seller-row">
                📞 ${h.phone}
            </div>

            <div class="seller-row">
                ✉️ ${h.email}
            </div>

            <div class="seller-row">
                💰 মূল্য:
                বিক্রেতার সাথে নিশ্চিত করুন
            </div>


            <button
                class="buy-btn"
                onclick="openOrder(${index})">

                🛒 অর্ডার করুন

            </button>

        </div>

    `;

}



/* =========================================================
   CURRENT SELLER
========================================================= */

let currentSeller = null;



/* =========================================================
   OPEN ORDER
========================================================= */

window.openOrder = function(index){

    const matched =
        HATCHERIES.filter(
            function(h){

                return (

                    h.division === division.value &&

                    h.district === district.value &&

                    h.upazila === upazila.value &&

                    h.fish.includes(fish.value)

                );

            }
        );


    currentSeller =
        matched[index];


    if(!currentSeller){

        return;

    }


    sellerInfo.innerHTML = `

        <strong>
            🏭 ${currentSeller.name}
        </strong>

        <br>

        📍 ${currentSeller.district},
        ${currentSeller.upazila}

        <br>

        🐟 মাছ:
        ${fish.value}

        <br>

        📞 ${currentSeller.phone}

    `;


    orderModal.classList.remove("hidden");

};



/* =========================================================
   CLOSE MODAL
========================================================= */

closeModal.addEventListener(
    "click",
    function(){

        orderModal.classList.add("hidden");

    }
);



orderModal.addEventListener(
    "click",
    function(event){

        if(event.target === orderModal){

            orderModal.classList.add("hidden");

        }

    }
);



/* =========================================================
   ORDER SUBMIT
========================================================= */

orderForm.addEventListener(
    "submit",
    function(event){

        event.preventDefault();


        const order = {

            id:Date.now(),

            seller:
                currentSeller.name,

            fish:
                fish.value,

            quantity:
                document
                .getElementById("quantity")
                .value,

            unit:
                document
                .getElementById("unit")
                .value,

            name:
                document
                .getElementById("buyerName")
                .value,

            phone:
                document
                .getElementById("buyerPhone")
                .value,

            address:
                document
                .getElementById("buyerAddress")
                .value,

            division:
                division.value,

            district:
                district.value,

            upazila:
                upazila.value,

            status:
                "অর্ডার রিকোয়েস্ট",

            date:
                new Date()
                .toLocaleString("bn-BD")

        };


        const orders =
            JSON.parse(
                localStorage.getItem(
                    "fishOrders"
                ) || "[]"
            );


        orders.unshift(order);


        localStorage.setItem(
            "fishOrders",
            JSON.stringify(orders)
        );


        orderForm.reset();


        orderModal.classList.add(
            "hidden"
        );


        renderOrders();


        alert(
            "✅ অর্ডার রিকোয়েস্ট সফলভাবে সংরক্ষণ হয়েছে।"
        );

    }
);



/* =========================================================
   SHOW ORDERS
========================================================= */

function renderOrders(){

    const orders =
        JSON.parse(
            localStorage.getItem(
                "fishOrders"
            ) || "[]"
        );


    const box =
        document.getElementById(
            "orders"
        );


    if(orders.length === 0){

        box.innerHTML = `

            <div class="empty">

                📦 এখনো কোনো অর্ডার নেই।

            </div>

        `;

        return;

    }


    box.innerHTML =
        orders.map(
            function(order){

                return `

                    <div class="order-card">

                        <strong>
                            🐟 ${order.fish}
                        </strong>

                        <br>

                        📦 পরিমাণ:
                        ${order.quantity}
                        ${order.unit}

                        <br>

                        🏭 বিক্রেতা:
                        ${order.seller}

                        <br>

                        👤 ক্রেতা:
                        ${order.name}

                        <br>

                        📞 মোবাইল:
                        ${order.phone}

                        <br>

                        📍 ঠিকানা:
                        ${order.address}

                        <br>

                        🗺️ এলাকা:
                        ${order.division}
                        →
                        ${order.district}
                        →
                        ${order.upazila}

                        <br>

                        🕒 সময়:
                        ${order.date}

                        <br>

                        🟢 অবস্থা:
                        ${order.status}

                    </div>

                `;

            }
        ).join("");

}



/* =========================================================
   START
========================================================= */

renderOrders();