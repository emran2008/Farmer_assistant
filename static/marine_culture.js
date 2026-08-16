/* =========================================================
   MARINE CULTURE SYSTEM
========================================================= */


/* =========================================================
   MARINE FISH DATABASE

   এগুলো preliminary screening values।
========================================================= */

const marineFishDatabase = {


    seabass:{
        name:"ভেটকি / এশিয়ান সিবাস",
        english:"Asian Seabass",
        temp:[26,32],
        salinity:[10,31],
        ph:[7.5,8.3],
        do:4,
        protein:40,
        methods:"Sea Cage / Coastal Cage / Marine Tank",
        feed:"High-protein floating pellet"
    },


    grouper:{
        name:"গ্রুপার",
        english:"Grouper",
        temp:[24,30],
        salinity:[15,35],
        ph:[7.5,8.5],
        do:4,
        protein:40,
        methods:"Sea Cage / Marine Tank",
        feed:"High-protein pellet / suitable fish feed"
    },


    pompano:{
        name:"পম্পানো",
        english:"Pompano",
        temp:[24,30],
        salinity:[20,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Sea Cage / Marine Tank",
        feed:"High-protein pellet"
    },


    cobia:{
        name:"কোবিয়া",
        english:"Cobia",
        temp:[24,32],
        salinity:[15,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Sea Cage / Marine Tank",
        feed:"High-protein pellet"
    },


    snapper:{
        name:"স্ন্যাপার",
        english:"Snapper",
        temp:[24,30],
        salinity:[25,35],
        ph:[7.8,8.5],
        do:5,
        protein:40,
        methods:"Sea Cage",
        feed:"High-protein pellet"
    },


    rabbitfish:{
        name:"র‍্যাবিটফিশ",
        english:"Rabbitfish",
        temp:[24,30],
        salinity:[25,35],
        ph:[7.8,8.5],
        do:5,
        protein:30,
        methods:"Sea Cage / Coastal Cage",
        feed:"Pellet + suitable plant-based feed"
    },


    milkfish:{
        name:"মিল্কফিশ",
        english:"Milkfish",
        temp:[24,32],
        salinity:[10,35],
        ph:[7.5,8.5],
        do:4,
        protein:30,
        methods:"Coastal Pond / Cage / Marine System",
        feed:"Pellet + natural food"
    },


    mullet:{
        name:"মুলেট / পারশে জাতীয় মাছ",
        english:"Mullet",
        temp:[22,30],
        salinity:[10,35],
        ph:[7.5,8.5],
        do:4,
        protein:30,
        methods:"Coastal Pond / Cage",
        feed:"Pellet + natural food"
    },


    seabream:{
        name:"সিব্রিম",
        english:"Sea Bream",
        temp:[20,28],
        salinity:[25,38],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Sea Cage / Marine Tank",
        feed:"High-protein pellet"
    },


    trevally:{
        name:"ট্রেভ্যালি",
        english:"Trevally",
        temp:[24,30],
        salinity:[25,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Sea Cage",
        feed:"High-protein pellet"
    },


    amberjack:{
        name:"অ্যাম্বারজ্যাক",
        english:"Amberjack",
        temp:[20,28],
        salinity:[25,38],
        ph:[7.5,8.5],
        do:5,
        protein:42,
        methods:"Sea Cage / Marine Tank",
        feed:"High-protein pellet"
    },


    yellowtail:{
        name:"ইয়েলোটেইল",
        english:"Yellowtail",
        temp:[18,26],
        salinity:[30,38],
        ph:[7.5,8.5],
        do:5,
        protein:42,
        methods:"Sea Cage",
        feed:"High-protein pellet"
    },


    barramundi:{
        name:"বারামুন্ডি",
        english:"Barramundi",
        temp:[26,32],
        salinity:[5,35],
        ph:[7,8.5],
        do:4,
        protein:40,
        methods:"Coastal Cage / Tank / RAS",
        feed:"High-protein pellet"
    },


    snubnose:{
        name:"স্নাবনোজ পম্পানো",
        english:"Snubnose Pompano",
        temp:[24,30],
        salinity:[20,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Sea Cage / Marine Tank",
        feed:"High-protein pellet"
    },


    silverpomfret:{
        name:"সাদা পমফ্রেট",
        english:"Silver Pomfret",
        temp:[24,30],
        salinity:[20,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Marine Cage / Marine Tank",
        feed:"Suitable marine fish feed"
    },


    blackpomfret:{
        name:"কালো পমফ্রেট",
        english:"Black Pomfret",
        temp:[24,30],
        salinity:[20,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Marine Cage / Marine Tank",
        feed:"Suitable marine fish feed"
    },


    croaker:{
        name:"কোরকার",
        english:"Croaker",
        temp:[22,30],
        salinity:[15,35],
        ph:[7.5,8.5],
        do:4,
        protein:35,
        methods:"Coastal Cage / Marine Tank",
        feed:"Pellet feed"
    },


    threadfin:{
        name:"থ্রেডফিন",
        english:"Threadfin",
        temp:[24,30],
        salinity:[20,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Marine Cage",
        feed:"High-protein feed"
    },


    emperor:{
        name:"এম্পেরর ফিশ",
        english:"Emperor Fish",
        temp:[23,30],
        salinity:[25,35],
        ph:[7.5,8.5],
        do:5,
        protein:38,
        methods:"Sea Cage",
        feed:"Marine pellet"
    },


    snapper2:{
        name:"রেড স্ন্যাপার",
        english:"Red Snapper",
        temp:[24,30],
        salinity:[25,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Sea Cage",
        feed:"High-protein pellet"
    },


    grouper2:{
        name:"টাইগার গ্রুপার",
        english:"Tiger Grouper",
        temp:[24,30],
        salinity:[20,35],
        ph:[7.5,8.5],
        do:4,
        protein:40,
        methods:"Marine Cage",
        feed:"High-protein feed"
    },


    queenfish:{
        name:"কুইনফিশ",
        english:"Queenfish",
        temp:[24,30],
        salinity:[20,35],
        ph:[7.5,8.5],
        do:5,
        protein:38,
        methods:"Coastal Cage / Marine Cage",
        feed:"Marine pellet"
    },


    pompano2:{
        name:"ফ্লোরিডা পম্পানো",
        english:"Florida Pompano",
        temp:[24,30],
        salinity:[20,35],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        methods:"Marine Cage / Tank",
        feed:"High-protein pellet"
    },


    mahi:{
        name:"মাহি-মাহি",
        english:"Mahi-Mahi",
        temp:[24,30],
        salinity:[28,38],
        ph:[7.8,8.5],
        do:5,
        protein:42,
        methods:"Marine Cage research/commercial systems",
        feed:"High-protein marine feed"
    },


    tuna:{
        name:"টুনা",
        english:"Tuna",
        temp:[20,30],
        salinity:[30,38],
        ph:[7.8,8.5],
        do:5,
        protein:45,
        methods:"Specialized marine systems",
        feed:"High-protein marine feed"
    }


};




const fishSelect =
document.getElementById("fishSelect");


Object.keys(marineFishDatabase)
.forEach(function(key){

    const fish =
    marineFishDatabase[key];


    const option =
    document.createElement("option");


    option.value = key;


    option.textContent =
    `${fish.name} (${fish.english})`;


    fishSelect.appendChild(option);

});





fishSelect.addEventListener(
    "change",
    showFishProfile
);


function showFishProfile(){

    const key =
    fishSelect.value;


    const box =
    document.getElementById("fishProfile");


    if(!key){

        box.classList.add("hidden");

        box.innerHTML = "";

        return;

    }


    const fish =
    marineFishDatabase[key];


    box.innerHTML = `

        <h3>
            🐟 ${fish.name}
        </h3>


        <div class="fish-profile-grid">


            <div class="profile-item">

                <b>🌡️ Temperature</b>

                ${fish.temp[0]}–${fish.temp[1]} °C

            </div>


            <div class="profile-item">

                <b>🧂 Salinity</b>

                ${fish.salinity[0]}–${fish.salinity[1]} ppt

            </div>


            <div class="profile-item">

                <b>🧪 pH</b>

                ${fish.ph[0]}–${fish.ph[1]}

            </div>


            <div class="profile-item">

                <b>💨 DO</b>

                ≥ ${fish.do} mg/L

            </div>


            <div class="profile-item">

                <b>🍚 Protein</b>

                প্রায় ${fish.protein}%

            </div>


            <div class="profile-item">

                <b>🌊 Culture</b>

                ${fish.methods}

            </div>


            <div class="profile-item">

                <b>🍽️ Feed</b>

                ${fish.feed}

            </div>


        </div>

    `;


    box.classList.remove("hidden");

}



/* =========================================================
   MAIN ANALYSIS
========================================================= */

function analyzeMarineCulture(){


    const fishKey =
    document.getElementById("fishSelect").value;


    if(!fishKey){

        alert(
            "⚠️ প্রথমে সামুদ্রিক মাছ নির্বাচন করুন।"
        );

        return;

    }


    const fish =
    marineFishDatabase[fishKey];


    const waterDepth =
    getNumber("waterDepth");


    const length =
    getNumber("cageLength");


    const width =
    getNumber("cageWidth");


    const depth =
    getNumber("cageDepth");


    const count =
    getNumber("fishCount");


    const weight =
    getNumber("fishWeight");


    const salinity =
    getNumber("salinity");


    const temperature =
    getNumber("temperature");


    const ph =
    getNumber("ph");


    const oxygen =
    getNumber("doValue");


    const ammonia =
    getNumber("ammonia");


    const nitrite =
    getNumber("nitrite");


    const transparency =
    getNumber("transparency");


    const protein =
    getNumber("protein");


    const mortality =
    getNumber("mortality");


    const current =
    document.getElementById("current").value;


    const wave =
    document.getElementById("wave").value;


    const pollution =
    document.getElementById("pollution").value;


    const waterExchange =
    document.getElementById("waterExchange").value;



    /* ===============================================
       BASIC VALIDATION
    =============================================== */

    if(
        length <= 0 ||
        width <= 0 ||
        depth <= 0 ||
        count <= 0 ||
        weight <= 0
    ){

        alert(
            "⚠️ খাঁচার মাপ এবং মাছের সংখ্যা/ওজন সঠিকভাবে দিন।"
        );

        return;

    }



    /* ===============================================
       VOLUME
    =============================================== */

    const volume =
    length * width * depth;



    /* ===============================================
       BIOMASS
    =============================================== */

    const biomass =
    (count * weight) / 1000;



    /* ===============================================
       DENSITY
    =============================================== */

    const density =
    count / volume;



    /* ===============================================
       FEED ESTIMATION
    =============================================== */

    let feedRate;


    if(weight < 50){

        feedRate = 0.06;

    }

    else if(weight < 100){

        feedRate = 0.045;

    }

    else if(weight < 300){

        feedRate = 0.03;

    }

    else{

        feedRate = 0.02;

    }


    const dailyFeed =
    biomass * 1000 * feedRate;



    /* ===============================================
       DISPLAY BASIC RESULTS
    =============================================== */

    document.getElementById(
        "volumeResult"
    ).textContent =
    `${volume.toFixed(2)} m³`;


    document.getElementById(
        "biomassResult"
    ).textContent =
    `${biomass.toFixed(2)} kg`;


    document.getElementById(
        "densityResult"
    ).textContent =
    `${density.toFixed(1)} মাছ/m³`;


    document.getElementById(
        "feedResult"
    ).textContent =
    `${dailyFeed.toFixed(0)} g/day`;



    /* ===============================================
       WATER ANALYSIS
    =============================================== */

    let waterHTML = [];


    waterHTML.push(

        waterCheck(
            "🧂 Salinity",
            salinity,
            `${fish.salinity[0]}–${fish.salinity[1]} ppt`,
            salinity >= fish.salinity[0] &&
            salinity <= fish.salinity[1]
        )

    );


    waterHTML.push(

        waterCheck(
            "🌡️ Temperature",
            temperature,
            `${fish.temp[0]}–${fish.temp[1]} °C`,
            temperature >= fish.temp[0] &&
            temperature <= fish.temp[1]
        )

    );


    waterHTML.push(

        waterCheck(
            "🧪 pH",
            ph,
            `${fish.ph[0]}–${fish.ph[1]}`,
            ph >= fish.ph[0] &&
            ph <= fish.ph[1]
        )

    );


    waterHTML.push(

        waterCheck(
            "💨 Dissolved Oxygen",
            oxygen,
            `≥ ${fish.do} mg/L`,
            oxygen >= fish.do
        )

    );


    waterHTML.push(

        waterCheck(
            "☠️ Ammonia",
            ammonia,
            "যত কম তত ভালো",
            ammonia <= 0.05
        )

    );


    waterHTML.push(

        waterCheck(
            "☠️ Nitrite",
            nitrite,
            "কম রাখা প্রয়োজন",
            nitrite <= 0.10
        )

    );


    if(transparency > 0){

        waterHTML.push(

            waterCheck(
                "💧 Transparency",
                transparency,
                "স্থানভেদে পরিবর্তনশীল",
                transparency >= 20
            )

        );

    }


    document.getElementById(
        "waterResults"
    ).innerHTML =
    waterHTML.join("");



    /* ===============================================
       SITE ANALYSIS
    =============================================== */

    let siteHTML = [];


    siteHTML.push(

        siteCheck(
            "🌊 Water Depth",
            `${waterDepth} m`,
            waterDepth >= 2
        )

    );


    siteHTML.push(

        siteCheck(
            "🌊 Current",
            current === "low"
            ? "কম"
            : current === "medium"
            ? "মাঝারি"
            : "বেশি",

            current !== "low"
        )

    );


    siteHTML.push(

        siteCheck(
            "🌪️ Wave",
            wave === "low"
            ? "কম"
            : wave === "medium"
            ? "মাঝারি"
            : "বেশি",

            wave !== "high"
        )

    );


    siteHTML.push(

        siteCheck(
            "🏭 Pollution",
            pollution === "low"
            ? "কম"
            : pollution === "medium"
            ? "মাঝারি"
            : "বেশি",

            pollution === "low"
        )

    );


    siteHTML.push(

        siteCheck(
            "💧 Water Exchange",
            waterExchange === "good"
            ? "ভালো"
            : waterExchange === "medium"
            ? "মাঝারি"
            : "কম",

            waterExchange === "good"
        )

    );


    document.getElementById(
        "siteResults"
    ).innerHTML =
    siteHTML.join("");



    /* ===============================================
       RISK ENGINE
    =============================================== */

    let risk = 0;

    let reasons = [];



    /* SALINITY */

    if(
        salinity < fish.salinity[0] ||
        salinity > fish.salinity[1]
    ){

        risk += 3;

        reasons.push(
            "Salinity অনুকূল range-এর বাইরে"
        );

    }



    /* TEMPERATURE */

    if(
        temperature < fish.temp[0] ||
        temperature > fish.temp[1]
    ){

        risk += 2;

        reasons.push(
            "Temperature অনুকূল নয়"
        );

    }



    /* PH */

    if(
        ph < fish.ph[0] ||
        ph > fish.ph[1]
    ){

        risk += 2;

        reasons.push(
            "pH অনুকূল নয়"
        );

    }



    /* DO */

    if(oxygen < fish.do){

        risk += 4;

        reasons.push(
            "DO কম"
        );

    }



    /* AMMONIA */

    if(ammonia > 0.05){

        risk += 3;

        reasons.push(
            "Ammonia বেশি"
        );

    }



    /* NITRITE */

    if(nitrite > 0.10){

        risk += 3;

        reasons.push(
            "Nitrite বেশি"
        );

    }



    /* WATER DEPTH */

    if(waterDepth < 2){

        risk += 2;

        reasons.push(
            "পানির গভীরতা কম"
        );

    }



    /* CURRENT */

    if(current === "low"){

        risk += 1;

        reasons.push(
            "পানির প্রবাহ কম"
        );

    }



    /* WAVES */

    if(wave === "high"){

        risk += 3;

        reasons.push(
            "ঢেউয়ের ঝুঁকি বেশি"
        );

    }



    /* POLLUTION */

    if(pollution === "high"){

        risk += 4;

        reasons.push(
            "পানি দূষণের ঝুঁকি বেশি"
        );

    }



    /* WATER EXCHANGE */

    if(waterExchange === "poor"){

        risk += 3;

        reasons.push(
            "Water exchange কম"
        );

    }



    /* MORTALITY */

    if(mortality > 3){

        risk += 4;

        reasons.push(
            "মৃত্যুহার বেশি"
        );

    }



    /* DENSITY */

    if(density > 150){

        risk += 2;

        reasons.push(
            "Stocking density বেশি"
        );

    }



    /* ===============================================
       PREDICTION
    =============================================== */

    let prediction;



    if(risk >= 12){

        prediction = `

            <div class="prediction danger">

                🚨

                <strong>
                    উচ্চ ঝুঁকি
                </strong>

                <br><br>

                বর্তমান তথ্য অনুযায়ী
                Marine Culture system-এ
                উল্লেখযোগ্য ঝুঁকি রয়েছে।

                <br><br>

                <strong>
                    প্রধান কারণ:
                </strong>

                <br>

                ${reasons.join(" • ")}

            </div>

        `;

    }


    else if(risk >= 6){

        prediction = `

            <div class="prediction warning">

                ⚠️

                <strong>
                    মাঝারি ঝুঁকি
                </strong>

                <br><br>

                কিছু পরিবেশগত ও
                ব্যবস্থাপনা বিষয় দ্রুত
                পর্যবেক্ষণ করা প্রয়োজন।

                <br><br>

                ${
                    reasons.length
                    ? reasons.join(" • ")
                    : "নিয়মিত পর্যবেক্ষণ চালিয়ে যান।"
                }

            </div>

        `;

    }


    else{

        prediction = `

            <div class="prediction good">

                ✅

                <strong>
                    বর্তমান অবস্থা গ্রহণযোগ্য
                </strong>

                <br><br>

                আপনার দেওয়া প্রধান
                পরিবেশগত তথ্য অনুযায়ী
                বড় ধরনের ঝুঁকি শনাক্ত হয়নি।

                <br><br>

                নিয়মিত পানি পরীক্ষা,
                feeding এবং মাছের আচরণ
                পর্যবেক্ষণ করুন।

            </div>

        `;

    }



    document.getElementById(
        "predictionBox"
    ).innerHTML =
    prediction;



    /* ===============================================
       FARMER ADVICE
    =============================================== */

    let advice = [];


    advice.push(
        "🌊 খাঁচা এমন জায়গায় রাখুন যেখানে পর্যাপ্ত পানির প্রবাহ থাকে কিন্তু অতিরিক্ত ঢেউ ও ঝড়ের ঝুঁকি কম।"
    );


    advice.push(
        "🧪 নিয়মিত Salinity, Temperature, pH এবং DO পরীক্ষা করুন।"
    );


    advice.push(
        "☠️ Ammonia ও Nitrite বাড়লে feed management এবং organic waste দ্রুত পরীক্ষা করুন।"
    );


    advice.push(
        "🪝 খাঁচার জাল নিয়মিত পরীক্ষা ও পরিষ্কার করুন যাতে biofouling পানির প্রবাহ কমিয়ে না দেয়।"
    );


    advice.push(
        "🐟 মাছের খাবার গ্রহণ, সাঁতারের আচরণ, surface gasping এবং অস্বাভাবিক মৃত্যু প্রতিদিন পর্যবেক্ষণ করুন।"
    );


    advice.push(
        "🍚 অতিরিক্ত feed দেবেন না; অবশিষ্ট feed পানির organic load বাড়াতে পারে।"
    );


    if(oxygen < fish.do){

        advice.push(
            "🚨 DO কম। পানির circulation বাড়ানোর সুযোগ, stocking density এবং রাত/ভোরের oxygen level পরীক্ষা করুন।"
        );

    }


    if(
        salinity < fish.salinity[0] ||
        salinity > fish.salinity[1]
    ){

        advice.push(
            "🧂 Salinity নির্বাচিত মাছের reference range-এর বাইরে। হঠাৎ salinity পরিবর্তনের কারণ পরীক্ষা করুন।"
        );

    }


    if(ammonia > 0.05){

        advice.push(
            "🚨 Ammonia বেশি। অতিরিক্ত feed, বর্জ্য এবং পানির বিনিময় ব্যবস্থা পরীক্ষা করুন।"
        );

    }


    if(nitrite > 0.10){

        advice.push(
            "🚨 Nitrite বেশি। পানির quality ও waste management দ্রুত পরীক্ষা করুন।"
        );

    }


    if(wave === "high"){

        advice.push(
            "🌪️ ঢেউ বেশি হলে cage frame, mooring, net এবং anchor system পরীক্ষা করুন।"
        );

    }


    if(pollution === "high"){

        advice.push(
            "🏭 দূষণের ঝুঁকি বেশি হলে পানির laboratory test করে source শনাক্ত করা প্রয়োজন।"
        );

    }


    if(mortality > 3){

        advice.push(
            "💀 মৃত্যুহার বেশি। মৃত মাছ দ্রুত অপসারণ করুন এবং রোগের কারণ নিশ্চিত করতে মৎস্য বিশেষজ্ঞ/ল্যাবের সহায়তা নিন।"
        );

    }


    advice.push(
        `🍚 নির্বাচিত ${fish.name}-এর জন্য database reference অনুযায়ী প্রায় ${fish.protein}% protein feed ব্যবহারের তথ্য রাখা হয়েছে; বয়স, আকার ও feed manufacturer-এর নির্দেশনা অনুযায়ী চূড়ান্ত feed নির্বাচন করুন।`
    );


    document.getElementById(
        "adviceList"
    ).innerHTML =

    advice.map(function(text){

        return `

            <div class="advice-item">

                <span class="advice-icon">
                    💡
                </span>

                <span>
                    ${text}
                </span>

            </div>

        `;

    }).join("");



    /* ===============================================
       SHOW RESULT
    =============================================== */

    document.getElementById(
        "resultSection"
    ).classList.remove("hidden");


    document.getElementById(
        "resultSection"
    ).scrollIntoView({

        behavior:"smooth"

    });

}



/* =========================================================
   WATER CHECK
========================================================= */

function waterCheck(
    title,
    value,
    ideal,
    okay
){

    const className =
    okay
    ? "good"
    : "danger";


    const status =
    okay
    ? "✅ গ্রহণযোগ্য"
    : "⚠️ পরীক্ষা প্রয়োজন";


    return `

        <div class="water-item ${className}">

            <h3>
                ${title}
            </h3>

            <strong>
                ${value}
            </strong>

            <br>

            Reference:
            ${ideal}

            <br>

            <strong>
                ${status}
            </strong>

        </div>

    `;

}



/* =========================================================
   SITE CHECK
========================================================= */

function siteCheck(
    title,
    value,
    okay
){

    const className =
    okay
    ? "good"
    : "warning";


    const status =
    okay
    ? "✅ ভালো"
    : "⚠️ পর্যবেক্ষণ প্রয়োজন";


    return `

        <div class="water-item ${className}">

            <h3>
                ${title}
            </h3>

            <strong>
                ${value}
            </strong>

            <br>

            <strong>
                ${status}
            </strong>

        </div>

    `;

}



/* =========================================================
   NUMBER HELPER
========================================================= */

function getNumber(id){

    const value =
    parseFloat(
        document.getElementById(id).value
    );


    return Number.isFinite(value)
    ? value
    : 0;

}



/* =========================================================
   BACK
========================================================= */

function goBack(){

    if(document.referrer){

        history.back();

    }

    else{

        window.location.href =
        "index.html";

    }

}