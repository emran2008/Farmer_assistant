/* =========================================================
   LIVESTOCK MANAGEMENT SYSTEM
========================================================= */


/* =========================================================
   ANIMAL DATA
========================================================= */

const livestock = {

    cattle: {

        name: "গরু",
        

        description:
            "দুধ, মাংস ও প্রজননের জন্য পালন করা হয়।",

        breeds: [

            "হলস্টেইন ফ্রিজিয়ান (Holstein Friesian)",
            "জার্সি (Jersey)",
            "সাহিওয়াল (Sahiwal)",
            "রেড চট্টগ্রাম (Red Chittagong Cattle)",
            "ব্রাহমান (Brahman)"

        ]

    },


    buffalo: {

        name: "মহিষ",
        

        description:
            "দুধ, মাংস ও কৃষিকাজের জন্য গুরুত্বপূর্ণ।",

        breeds: [

            "মুররাহ (Murrah)",
            "নিলি-রাভি (Nili-Ravi)",
            "জাফরাবাদি (Jaffarabadi)",
            "মেহসানা (Mehsana)",
            "সুরতি (Surti)"

        ]

    },


    goat: {

        name: "ছাগল",
        

        description:
            "মাংস, দুধ ও প্রজননের জন্য জনপ্রিয়।",

        breeds: [

            "ব্ল্যাক বেঙ্গল (Black Bengal)",
            "জামুনাপারি (Jamunapari)",
            "বিটাল (Beetal)",
            "সিরোহি (Sirohi)",
            "টোজেনবার্গ (Toggenburg)",
            "অ্যাংলো-নুবিয়ান (Anglo-Nubian)"

        ]

    },


    sheep: {

        name: "ভেড়া",
        

        description:
            "মাংস, পশম ও প্রজননের জন্য পালন করা হয়।",

        breeds: [

            "দেশি ভেড়া (Bangladeshi Local Sheep)",
            "গারোল (Garole)",
            "বারিন্দি ভেড়া (Barind Sheep)",
            "কাজলি ভেড়া (Kajli)",
            "দর্পার (Dorper)",
            "মেরিনো (Merino)"

        ]

    },


    horse: {

        name: "ঘোড়া",
        

        description:
            "পরিবহন, ক্রীড়া ও প্রজননের জন্য পালন করা হয়।",

        breeds: [

            "বাংলাদেশি দেশি ঘোড়া (Local Bangladeshi Horse)",
            "আরবীয় ঘোড়া (Arabian)",
            "থরোব্রেড (Thoroughbred)",
            "কাঠিয়াওয়ারি (Kathiawari)",
            "মারওয়ারি (Marwari)"

        ]

    },


    donkey: {

        name: "গাধা",
        

        description:
            "শ্রম ও পরিবহনের কাজে ব্যবহৃত হয়।",

        breeds: [

            "দেশি গাধা (Local Donkey)",
            "ইন্ডিয়ান ওয়াইল্ড অ্যাস (Indian Wild Ass)",
            "ম্যামথ জ্যাকস্টক (Mammoth Jackstock)",
            "পোয়াটু (Poitevin)",
            "অ্যান্ডালুসিয়ান গাধা (Andalusian Donkey)"

        ]

    },


    camel: {

        name: "উট",
        

        description:
            "শুষ্ক ও উষ্ণ পরিবেশে অভিযোজিত প্রাণী।",

        breeds: [

            "আরবীয় উট / ড্রোমেডারি (Dromedary)",
            "বাকট্রিয়ান উট (Bactrian)",
            "মায়ান উট (Maya Camel)",
            "সোমালি উট (Somali Camel)",
            "সুদানি উট (Sudanese Camel)"

        ]

    },


    pig: {

        name: "শূকর",
        

        description:
            "মাংস উৎপাদনের জন্য পালন করা হয়।",

        breeds: [

            "দেশি শূকর (Local Pig)",
            "হ্যাম্পশায়ার (Hampshire)",
            "ইয়র্কশায়ার / লার্জ হোয়াইট (Yorkshire / Large White)",
            "ল্যান্ডরেস (Landrace)",
            "ডুরক (Duroc)"

        ]

    },


    chicken: {

        name: "মুরগি",
        

        description:
            "মাংস ও ডিম উৎপাদনের অন্যতম প্রধান পাখি।",

        breeds: [

            "দেশি মুরগি (Deshi Chicken)",
            "সোনালি (Sonali)",
            "ফাউমি (Fayoumi)",
            "রোড আইল্যান্ড রেড (Rhode Island Red)",
            "লেগহর্ন (Leghorn)",
            "ব্রয়লার (Broiler)",
            "হোয়াইট লেগহর্ন (White Leghorn)",
            "অস্ট্রালর্প (Australorp)"

        ]

    },


    duck: {

        name: "হাঁস",
        

        description:
            "ডিম ও মাংসের জন্য পালন করা হয়।",

        breeds: [

            "খাকি ক্যাম্পবেল (Khaki Campbell)",
            "ইন্ডিয়ান রানার (Indian Runner)",
            "দেশি হাঁস (Deshi Duck)",
            "জিংডিং (Jinding)",
            "মাসকোভি (Muscovy Duck)",
            "পেকিন (Pekin Duck)",
            "সিলেট মেট (Sylhet Mete)"

        ]

    },


    pigeon: {

        name: "কবুতর",
        

        description:
            "শখ, মাংস ও প্রজননের জন্য পালন করা হয়।",

        breeds: [

            "গোলা (Gola)",
            "গিরিবাজ (Giribaaz)",
            "হোমার (Homer)",
            "কিং (King)",
            "মন্ডেইন (Mondain)",
            "ফ্যানটেল (Fantail)",
            "লাহোরি (Lahore)",
            "সিরাজি (Shirazi)"

        ]

    },


    rabbit: {

        name: "খরগোশ",
        

        description:
            "মাংস, প্রজনন ও শখের জন্য পালন করা হয়।",

        breeds: [

            "নিউজিল্যান্ড হোয়াইট (New Zealand White)",
            "ক্যালিফোর্নিয়ান (Californian)",
            "ডাচ (Dutch)",
            "ফ্লেমিশ জায়ান্ট (Flemish Giant)",
            "চিনচিলা (Chinchilla)",
            "সোভিয়েত চিনচিলা (Soviet Chinchilla)"

        ]

    },


    deer: {

        name: "হরিণ",
        

        description:
            "বন্যপ্রাণী ও নির্দিষ্ট অনুমোদিত ব্যবস্থাপনায় পালনযোগ্য।",

        breeds: [

            "চিত্রা হরিণ (Chital / Spotted Deer)",
            "সাম্বার হরিণ (Sambar Deer)",
            "মায়া হরিণ (Barking Deer)",
            "পারা হরিণ (Hog Deer)"

        ]

    },


    turkey: {

        name: "টার্কি",
        

        description:
            "মাংস উৎপাদনের জন্য পালন করা হয়।",

        breeds: [

            "ব্রড ব্রেস্টেড হোয়াইট (Broad Breasted White)",
            "ব্রড ব্রেস্টেড ব্রোঞ্জ (Broad Breasted Bronze)",
            "বেল্টসভিল স্মল হোয়াইট (Beltsville Small White)",
            "ন্যারাগানসেট (Narragansett)",
            "ব্ল্যাক টার্কি (Black Turkey)"

        ]

    },


    peacock: {

        name: "ময়ূর",
        

        description:
            "শোভাময় ও সংরক্ষণমূলক ব্যবস্থাপনায় পরিচিত পাখি।",

        breeds: [

            "ভারতীয় নীল ময়ূর (Indian Peafowl / Blue Peafowl)",
            "সবুজ ময়ূর (Green Peafowl)",
            "কঙ্গো ময়ূর (Congo Peafowl)"

        ]

    },


    llama: {

        name: "লামা",
        

        description:
            "পশম, প্রদর্শনী ও নির্দিষ্ট খামারি ব্যবস্থাপনায় পালন করা হয়।",

        breeds: [

            "ক্লাসিক লামা (Classic Llama)",
            "উলি লামা (Wooly Llama)",
            "সুরি লামা (Suri Llama)",
            "সুরকো লামা (Surco Type)",
            "মিডিয়াম লামা (Medium Llama)"

        ]

    }

};


/* =========================================================
   GENERAL SPECIES INFORMATION
========================================================= */

const speciesInfo = {


    cattle: {

        temperature: "প্রায় 15–30°C; অতিরিক্ত গরমে ছায়া ও বাতাস চলাচল প্রয়োজন",

        water: "পরিষ্কার পানি সবসময় রাখতে হবে। দুধাল গাভীর পানির চাহিদা বেশি।",

        feed: "সবুজ ঘাস, শুকনা খড়, সুষম কনসেনট্রেট, মিনারেল ও লবণ।",

        housing: "শুকনা, পরিষ্কার, বাতাস চলাচলকারী গোয়ালঘর।",

        management: [
            "প্রতিদিন গোয়ালঘর পরিষ্কার করতে হবে।",
            "অসুস্থ প্রাণী আলাদা রাখতে হবে।",
            "খাদ্য ধীরে ধীরে পরিবর্তন করতে হবে।",
            "নিয়মিত ওজন/শারীরিক অবস্থা পর্যবেক্ষণ করতে হবে।"
        ],

        feeding: [
            "সবুজ ঘাস",
            "খড়",
            "কনসেনট্রেট ফিড",
            "মিনারেল মিক্স",
            "লবণ"
        ],

        environment: [
            "পরিষ্কার পানি",
            "বাতাস চলাচল",
            "গরমে ছায়া",
            "বৃষ্টির পানি জমতে না দেওয়া"
        ],

        diseases: [
            {
                name: "ক্ষুরা রোগ (FMD)",
                symptoms: "জ্বর, মুখে লালা, মুখ ও পায়ে ক্ষত/ফোসকা।",
                prevention: "টিকাদান, আক্রান্ত পশু পৃথকীকরণ ও খামারে বায়োসিকিউরিটি।"
            },
            {
                name: "ক্ষুর ও মুখের সমস্যা",
                symptoms: "খোঁড়ানো, খাবার কম খাওয়া।",
                prevention: "পরিষ্কার মেঝে ও নিয়মিত খুর পরীক্ষা।"
            },
            {
                name: "মাস্টাইটিস",
                symptoms: "স্তন ফুলে যাওয়া, দুধের পরিবর্তন।",
                prevention: "দোহনের আগে-পরে পরিষ্কার-পরিচ্ছন্নতা।"
            },
            {
                name: "কৃমি সংক্রমণ",
                symptoms: "ওজন কমা, দুর্বলতা, ডায়রিয়া।",
                prevention: "ভেটেরিনারি পরামর্শে কৃমিনাশক।"
            }
        ],

        vaccination: [
            ["বাছুর বয়স অনুযায়ী", "FMD", "ক্ষুরা রোগ প্রতিরোধ", "স্থানীয় সরকারি সূচি"],
            ["প্রাপ্তবয়স্ক", "FMD booster", "ক্ষুরা রোগ প্রতিরোধ", "সরকারি/ভেটেরিনারি সূচি"],
            ["ঝুঁকিপূর্ণ এলাকায়", "Anthrax", "অ্যানথ্রাক্স প্রতিরোধ", "স্থানীয় নির্দেশনা"]
        ],

        breeding:
            "সুস্থ ও রোগমুক্ত প্রজননযোগ্য প্রাণী নির্বাচন করতে হবে। কৃত্রিম প্রজনন বা প্রাকৃতিক প্রজনন উভয়ই ব্যবহৃত হতে পারে।",

        production:
            "দুধ, মাংস, বাছুর এবং প্রজনন মূল্য।",

        warnings: [
            "অসুস্থ পশুর দুধ/মাংস ব্যবহারের আগে ভেটেরিনারি পরামর্শ নিন।",
            "নিজে থেকে অ্যান্টিবায়োটিক ব্যবহার করবেন না।",
            "টিকার সময়সূচি স্থানীয় কর্তৃপক্ষের সাথে মিলিয়ে নিন।"
        ]

    },


    buffalo: {

        temperature: "প্রায় 18–30°C; গরমে ছায়া ও পানিতে ঠান্ডা হওয়ার সুযোগ উপকারী।",

        water: "সবসময় পরিষ্কার পানি।",

        feed: "সবুজ ঘাস, খড়, কনসেনট্রেট, মিনারেল।",

        housing: "পরিষ্কার ও বাতাস চলাচলকারী শেড।",

        management: [
            "গরমে heat stress কমাতে ছায়া ও পর্যাপ্ত পানি দিন।",
            "নিয়মিত শরীরের অবস্থা পর্যবেক্ষণ করুন।",
            "পরিষ্কার দোহন ব্যবস্থা বজায় রাখুন।"
        ],

        feeding: [
            "সবুজ ঘাস",
            "খড়",
            "কনসেনট্রেট",
            "মিনারেল মিক্স"
        ],

        environment: [
            "ছায়া",
            "পরিষ্কার পানি",
            "ভালো বায়ু চলাচল"
        ],

        diseases: [
            {
                name: "ক্ষুরা রোগ",
                symptoms: "জ্বর, মুখ ও পায়ে ক্ষত।",
                prevention: "টিকা ও বায়োসিকিউরিটি।"
            },
            {
                name: "মাস্টাইটিস",
                symptoms: "স্তন ফুলে যাওয়া ও দুধের পরিবর্তন।",
                prevention: "দোহনের স্বাস্থ্যবিধি।"
            },
            {
                name: "কৃমি",
                symptoms: "দুর্বলতা ও ওজন কমা।",
                prevention: "ভেটেরিনারি পরামর্শে নিয়ন্ত্রণ।"
            }
        ],

        vaccination: [
            ["স্থানীয় সূচি অনুযায়ী", "FMD", "ক্ষুরা রোগ", "ভেটেরিনারি নির্দেশনা"],
            ["ঝুঁকিপূর্ণ এলাকায়", "Anthrax", "অ্যানথ্রাক্স", "স্থানীয় নির্দেশনা"]
        ],

        breeding:
            "সুস্থ ও ভালো উৎপাদনক্ষম প্রাণী নির্বাচন করুন।",

        production:
            "দুধ, মাংস ও প্রজনন।",

        warnings: [
            "অতিরিক্ত গরমে heat stress হতে পারে।",
            "অসুস্থ প্রাণী আলাদা রাখুন।"
        ]

    },


    goat: {

        temperature: "প্রায় 15–30°C; শুকনা পরিবেশ ভালো।",

        water: "সবসময় পরিষ্কার পানি।",

        feed: "ঘাস, পাতা, গাছের কচি অংশ, খড় ও সুষম ফিড।",

        housing: "উঁচু, শুকনা ও বাতাস চলাচলকারী ঘর।",

        management: [
            "ভেজা মেঝে এড়িয়ে চলুন।",
            "নতুন ছাগল আলাদা পর্যবেক্ষণে রাখুন।",
            "খুর নিয়মিত পরীক্ষা করুন।"
        ],

        feeding: [
            "সবুজ ঘাস",
            "পাতা",
            "খড়",
            "কনসেনট্রেট",
            "মিনারেল"
        ],

        environment: [
            "শুকনা ঘর",
            "পরিষ্কার পানি",
            "পর্যাপ্ত বাতাস"
        ],

        diseases: [
            {
                name: "PPR",
                symptoms: "জ্বর, নাক দিয়ে স্রাব, মুখে ক্ষত, ডায়রিয়া।",
                prevention: "টিকাদান ও আক্রান্ত প্রাণী পৃথক রাখা।"
            },
            {
                name: "কৃমি",
                symptoms: "ওজন কমা, দুর্বলতা, ডায়রিয়া।",
                prevention: "ভেটেরিনারি পরামর্শ অনুযায়ী কৃমি নিয়ন্ত্রণ।"
            },
            {
                name: "Foot rot",
                symptoms: "খোঁড়ানো ও খুরে সমস্যা।",
                prevention: "শুকনা ও পরিষ্কার মেঝে।"
            }
        ],

        vaccination: [
            ["স্থানীয় সূচি", "PPR", "PPR প্রতিরোধ", "সরকারি/ভেটেরিনারি নির্দেশনা"],
            ["ঝুঁকি অনুযায়ী", "FMD", "ক্ষুরা রোগ", "স্থানীয় সূচি"]
        ],

        breeding:
            "প্রজননের জন্য সুস্থ, সক্রিয় ও রোগমুক্ত প্রাণী নির্বাচন করুন।",

        production:
            "মাংস, দুধ ও বাচ্চা উৎপাদন।",

        warnings: [
            "অতিরিক্ত ভেজা পরিবেশ এড়িয়ে চলুন।",
            "কৃমিনাশক ব্যবহারে স্থানীয় ভেটেরিনারি পরামর্শ নিন।"
        ]

    },


    sheep: {

        temperature: "প্রায় 15–30°C; গরমে ছায়া প্রয়োজন।",

        water: "পরিষ্কার পানি সবসময়।",

        feed: "ঘাস, খড়, পাতা ও সুষম খাদ্য।",

        housing: "শুকনা, উঁচু ও পরিষ্কার শেড।",

        management: [
            "নিয়মিত পশম ও চামড়া পরীক্ষা করুন।",
            "খুর পরীক্ষা করুন।",
            "নতুন প্রাণী quarantine করুন।"
        ],

        feeding: [
            "চারণ ঘাস",
            "খড়",
            "পাতা",
            "সুষম ফিড"
        ],

        environment: [
            "শুকনা ঘর",
            "বাতাস চলাচল",
            "পরিষ্কার পানি"
        ],

        diseases: [
            {
                name: "PPR",
                symptoms: "জ্বর, নাক দিয়ে স্রাব, ডায়রিয়া।",
                prevention: "টিকা ও বায়োসিকিউরিটি।"
            },
            {
                name: "কৃমি",
                symptoms: "দুর্বলতা ও ওজন কমা।",
                prevention: "পরিকল্পিত parasite control।"
            }
        ],

        vaccination: [
            ["স্থানীয় সূচি", "PPR", "PPR প্রতিরোধ", "ভেটেরিনারি নির্দেশনা"],
            ["ঝুঁকি অনুযায়ী", "FMD", "ক্ষুরা রোগ", "স্থানীয় নির্দেশনা"]
        ],

        breeding:
            "সুস্থ ও ভালো গঠনযুক্ত প্রাণী নির্বাচন করুন।",

        production:
            "মাংস, পশম ও প্রজনন।",

        warnings: [
            "অতিরিক্ত কাদা ও ভেজা পরিবেশ এড়িয়ে চলুন।"
        ]

    },


    chicken: {

        temperature: "বয়স অনুযায়ী পরিবর্তনশীল; বাচ্চার জন্য ব্রুডিং তাপমাত্রা নিয়ন্ত্রণ জরুরি।",

        water: "পরিষ্কার ও ঠান্ডা/স্বাভাবিক তাপমাত্রার পানি সবসময়।",

        feed: "Starter → Grower → Layer/Finisher অনুযায়ী সুষম খাদ্য।",

        housing: "শুকনা, পরিষ্কার, পর্যাপ্ত বাতাস চলাচলকারী ঘর।",

        management: [
            "বাচ্চার জন্য ব্রুডিং ব্যবস্থা রাখতে হবে।",
            "ঘরের তাপমাত্রা ও আর্দ্রতা পর্যবেক্ষণ করুন।",
            "নতুন পাখি quarantine করুন।",
            "Feed ও water feeder নিয়মিত পরিষ্কার করুন।"
        ],

        feeding: [
            "Chick starter",
            "Grower feed",
            "Layer feed",
            "Broiler finisher",
            "মিনারেল ও ভিটামিন প্রয়োজন অনুযায়ী"
        ],

        environment: [
            "পরিষ্কার লিটার",
            "ভালো ventilation",
            "অতিরিক্ত গরমে cooling ব্যবস্থা",
            "পরিষ্কার পানি"
        ],

        diseases: [
            {
                name: "Newcastle Disease",
                symptoms: "শ্বাসকষ্ট, স্নায়বিক সমস্যা, মৃত্যু হতে পারে।",
                prevention: "নিয়মিত টিকা ও biosecurity।"
            },
            {
                name: "Gumboro / IBD",
                symptoms: "দুর্বলতা, ডায়রিয়া, পালক এলোমেলো।",
                prevention: "ফার্মের টিকা পরিকল্পনা।"
            },
            {
                name: "Coccidiosis",
                symptoms: "ডায়রিয়া, রক্ত মিশ্রিত পায়খানা হতে পারে।",
                prevention: "শুকনা লিটার ও সঠিক ব্যবস্থাপনা।"
            },
            {
                name: "Respiratory disease",
                symptoms: "হাঁচি, নাক দিয়ে স্রাব, শ্বাসকষ্ট।",
                prevention: "ভালো ventilation ও biosecurity।"
            }
        ],

        vaccination: [
            ["বাচ্চার বয়স অনুযায়ী", "Marek's", "Marek's disease", "ভেটেরিনারি/হ্যাচারি সূচি"],
            ["প্রাথমিক বয়স", "ND", "Newcastle Disease", "ফার্মের সূচি"],
            ["পরবর্তী বয়স", "IBD", "Gumboro", "ফার্মের সূচি"],
            ["পরবর্তী পর্যায়", "ND/অন্যান্য", "রোগ প্রতিরোধ", "স্থানীয় ভেটেরিনারি সূচি"]
        ],

        breeding:
            "ডিম উৎপাদনকারী জাতের ক্ষেত্রে ভালো breeder flock নির্বাচন গুরুত্বপূর্ণ।",

        production:
            "ডিম ও মাংস।",

        warnings: [
            "এক ফার্মের সরঞ্জাম অন্য ফার্মে না নেওয়া ভালো।",
            "অ্যান্টিবায়োটিক নিজের সিদ্ধান্তে ব্যবহার করবেন না।"
        ]

    },


    duck: {

        temperature: "বাচ্চার বয়স অনুযায়ী brooding প্রয়োজন; প্রাপ্তবয়স্ক হাঁস তুলনামূলক সহনশীল।",

        water: "পরিষ্কার পানীয় পানি সবসময়।",

        feed: "Duck starter/grower/layer feed, শস্য ও প্রয়োজনীয় পুষ্টি।",

        housing: "শুকনা ঘর এবং পর্যাপ্ত ventilation।",

        management: [
            "পানি ও খাবারের জায়গা পরিষ্কার রাখুন।",
            "ভেজা লিটার দ্রুত পরিবর্তন করুন।",
            "বাচ্চার জন্য তাপ নিয়ন্ত্রণ করুন।"
        ],

        feeding: [
            "Duck starter",
            "Grower feed",
            "Layer feed",
            "শস্য",
            "মিনারেল"
        ],

        environment: [
            "পরিষ্কার পানি",
            "শুকনা লিটার",
            "বাতাস চলাচল"
        ],

        diseases: [
            {
                name: "Duck plague",
                symptoms: "দুর্বলতা, ডায়রিয়া, মৃত্যু হতে পারে।",
                prevention: "টিকা ও biosecurity।"
            },
            {
                name: "কলেরা",
                symptoms: "জ্বর, দুর্বলতা ও আকস্মিক মৃত্যু।",
                prevention: "পরিষ্কার পরিবেশ ও ভেটেরিনারি ব্যবস্থাপনা।"
            }
        ],

        vaccination: [
            ["স্থানীয় সূচি", "Duck plague vaccine", "Duck plague প্রতিরোধ", "ভেটেরিনারি নির্দেশনা"],
            ["ঝুঁকি অনুযায়ী", "Duck cholera", "কলেরা প্রতিরোধ", "স্থানীয় নির্দেশনা"]
        ],

        breeding:
            "ভালো ডিম উৎপাদন ও স্বাস্থ্যসম্পন্ন breeder নির্বাচন করুন।",

        production:
            "ডিম ও মাংস।",

        warnings: [
            "পানির উৎস নোংরা হলে রোগ ছড়াতে পারে।"
        ]

    }

};


/* =========================================================
   DEFAULT DATA FOR OTHER ANIMALS
========================================================= */

const defaultInfo = {

    temperature: "স্থানীয় পরিবেশ অনুযায়ী উপযুক্ত তাপমাত্রা বজায় রাখতে হবে।",

    water: "সবসময় পরিষ্কার ও নিরাপদ পানীয় পানি রাখতে হবে।",

    feed: "প্রজাতি ও বয়স অনুযায়ী সুষম খাদ্য দিতে হবে।",

    housing: "শুকনা, পরিষ্কার ও পর্যাপ্ত বাতাস চলাচলকারী বাসস্থান প্রয়োজন।",

    management: [
        "প্রতিদিন প্রাণীর স্বাস্থ্য পরীক্ষা করুন।",
        "পরিষ্কার-পরিচ্ছন্নতা বজায় রাখুন।",
        "অসুস্থ প্রাণী আলাদা করুন।",
        "নতুন প্রাণী কিছুদিন পর্যবেক্ষণে রাখুন।"
    ],

    feeding: [
        "বয়স অনুযায়ী সুষম খাদ্য",
        "পরিষ্কার পানি",
        "প্রয়োজন অনুযায়ী মিনারেল ও ভিটামিন"
    ],

    environment: [
        "পরিষ্কার পরিবেশ",
        "ভালো ventilation",
        "অতিরিক্ত গরম/ঠান্ডা থেকে সুরক্ষা"
    ],

    diseases: [
        {
            name: "পরজীবী সংক্রমণ",
            symptoms: "দুর্বলতা, ওজন কমা, খাবার কম খাওয়া।",
            prevention: "পরিষ্কার পরিবেশ ও ভেটেরিনারি parasite control।"
        },
        {
            name: "শ্বাসতন্ত্রের সমস্যা",
            symptoms: "হাঁচি, নাক দিয়ে স্রাব, শ্বাসকষ্ট।",
            prevention: "ভালো ventilation ও biosecurity।"
        }
    ],

    vaccination: [
        [
            "প্রজাতি ও বয়স অনুযায়ী",
            "প্রযোজ্য টিকা",
            "রোগ প্রতিরোধ",
            "স্থানীয় ভেটেরিনারি সূচি"
        ]
    ],

    breeding:
        "সুস্থ, রোগমুক্ত ও কাঙ্ক্ষিত বৈশিষ্ট্যের প্রাণী নির্বাচন করা উচিত।",

    production:
        "জাতভেদে মাংস, দুধ, ডিম, পশম, প্রজনন বা অন্যান্য ব্যবহার।",

    warnings: [
        "রোগের লক্ষণ দেখা দিলে দ্রুত ভেটেরিনারি চিকিৎসকের পরামর্শ নিন।",
        "নিজে থেকে অ্যান্টিবায়োটিক বা অন্য ওষুধ প্রয়োগ করবেন না।",
        "টিকার সময়সূচি স্থানীয় সরকারি/ভেটেরিনারি নির্দেশনার সাথে মিলিয়ে নিন।"
    ]

};


/* =========================================================
   VARIABLES
========================================================= */

let selectedAnimalKey = null;

let selectedBreedName = null;


/* =========================================================
   INITIALIZE
========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    renderAnimals();

});


/* =========================================================
   SHOW ANIMALS
========================================================= */

function renderAnimals() {

    const grid =
        document.getElementById("animalGrid");

    grid.innerHTML = "";

    Object.entries(livestock).forEach(
        ([key, animal]) => {

            const card =
                document.createElement("div");

            card.className = "animal-card";

            card.innerHTML = `

                <div class="icon">
                    
                </div>

                <h3>
                    ${animal.name}
                </h3>

                <p>
                    ${animal.breeds.length}
                    টি জাত
                </p>

            `;

            card.onclick = () =>
                openAnimal(key);

            grid.appendChild(card);

        }
    );

}


/* =========================================================
   OPEN ANIMAL
========================================================= */

function openAnimal(key) {

    selectedAnimalKey = key;

    const animal =
        livestock[key];

    document
        .getElementById("animalHome")
        .classList.add("hidden");

    document
        .getElementById("detailPage")
        .classList.add("hidden");

    document
        .getElementById("breedPage")
        .classList.remove("hidden");


    document
        .getElementById("selectedAnimalIcon")
        .textContent = animal.icon;


    document
        .getElementById("selectedAnimalName")
        .textContent = animal.name;


    document
        .getElementById("selectedAnimalDescription")
        .textContent = animal.description;


    renderBreeds(key);

}


/* =========================================================
   RENDER BREEDS
========================================================= */

function renderBreeds(key) {

    const grid =
        document.getElementById("breedGrid");

    grid.innerHTML = "";

    livestock[key].breeds.forEach(
        breed => {

            const card =
                document.createElement("div");

            card.className =
                "breed-card";

            card.innerHTML = `

                <h3>
                    ${breed}
                </h3>

                <p>
                    বিস্তারিত তথ্য দেখতে ক্লিক করুন →
                </p>

            `;

            card.onclick = () =>
                openBreed(breed);

            grid.appendChild(card);

        }
    );

}


/* =========================================================
   OPEN BREED
========================================================= */

function openBreed(breedName) {

    selectedBreedName =
        breedName;

    const animal =
        livestock[selectedAnimalKey];

    const data =
        speciesInfo[selectedAnimalKey]
        || defaultInfo;


    document
        .getElementById("breedPage")
        .classList.add("hidden");

    document
        .getElementById("detailPage")
        .classList.remove("hidden");


    document
        .getElementById("detailIcon")
        .textContent =
        animal.icon;


    document
        .getElementById("detailBreedName")
        .textContent =
        breedName;


    document
        .getElementById("detailScientificName")
        .textContent =
        animal.name +
        " — পালন ও ব্যবস্থাপনা";


    /* QUICK INFO */

    document
        .getElementById("temperature")
        .textContent =
        data.temperature;


    document
        .getElementById("water")
        .textContent =
        data.water;


    document
        .getElementById("feed")
        .textContent =
        data.feed;


    document
        .getElementById("housing")
        .textContent =
        data.housing;


    /* MANAGEMENT */

    document
        .getElementById("management")
        .innerHTML =
        createList(data.management);


    /* FEEDING */

    document
        .getElementById("feeding")
        .innerHTML =
        createList(data.feeding);


    /* ENVIRONMENT */

    document
        .getElementById("environment")
        .innerHTML =
        createList(data.environment);


    /* DISEASE */

    renderDiseases(data.diseases);


    /* VACCINATION */

    renderVaccination(data.vaccination);


    /* BREEDING */

    document
        .getElementById("breeding")
        .innerHTML =
        `<p>${data.breeding}</p>`;


    /* PRODUCTION */

    document
        .getElementById("production")
        .innerHTML =
        `<p>${data.production}</p>`;


    /* WARNINGS */

    document
        .getElementById("warnings")
        .innerHTML =
        data.warnings
            .map(item => `<li>${item}</li>`)
            .join("");

}


/* =========================================================
   CREATE LIST
========================================================= */

function createList(items) {

    return `

        <ul>

            ${items
                .map(item =>
                    `<li>${item}</li>`
                )
                .join("")}

        </ul>

    `;

}


/* =========================================================
   DISEASE RENDER
========================================================= */

function renderDiseases(diseases) {

    const box =
        document.getElementById("diseases");

    box.innerHTML = "";

    diseases.forEach(disease => {

        const div =
            document.createElement("div");

        div.className =
            "disease-card";

        div.innerHTML = `

            <h4>
                 ${disease.name}
            </h4>

            <p>
                <strong>লক্ষণ:</strong>
                ${disease.symptoms}
            </p>

            <p>
                <strong>প্রতিরোধ:</strong>
                ${disease.prevention}
            </p>

        `;

        box.appendChild(div);

    });

}


/* =========================================================
   VACCINATION RENDER
========================================================= */

function renderVaccination(vaccines) {

    const table =
        document.getElementById(
            "vaccinationTable"
        );

    table.innerHTML = "";

    vaccines.forEach(row => {

        const tr =
            document.createElement("tr");

        row.forEach(cell => {

            const td =
                document.createElement("td");

            td.textContent = cell;

            tr.appendChild(td);

        });

        table.appendChild(tr);

    });

}


/* =========================================================
   SHOW BREEDS
========================================================= */

function showBreeds() {

    document
        .getElementById("detailPage")
        .classList.add("hidden");

    document
        .getElementById("breedPage")
        .classList.remove("hidden");

}


/* =========================================================
   SHOW ANIMALS
========================================================= */

function showAnimals() {

    document
        .getElementById("breedPage")
        .classList.add("hidden");

    document
        .getElementById("detailPage")
        .classList.add("hidden");

    document
        .getElementById("animalHome")
        .classList.remove("hidden");

}