/* =====================================================
   CAGE CULTURE SYSTEM
===================================================== */


/* =====================================================
   FISH DATABASE
===================================================== */

const fishDatabase = {

    tilapia:{
        name:"তেলাপিয়া",
        english:"Tilapia",
        temperature:[25,32],
        ph:[6.5,8.5],
        do:4,
        protein:30,
        feed:"ভাসমান পিলেট ফিড"
    },

    pangasius:{
        name:"পাঙ্গাস",
        english:"Pangasius",
        temperature:[26,32],
        ph:[6.5,8],
        do:4,
        protein:28,
        feed:"পিলেট ফিড"
    },

    rohu:{
        name:"রুই",
        english:"Rohu",
        temperature:[24,30],
        ph:[6.5,8.5],
        do:5,
        protein:28,
        feed:"পিলেট + প্রাকৃতিক খাদ্য"
    },

    catla:{
        name:"কাতলা",
        english:"Catla",
        temperature:[24,30],
        ph:[6.5,8.5],
        do:5,
        protein:28,
        feed:"পিলেট + প্রাকৃতিক খাদ্য"
    },

    mrigal:{
        name:"মৃগেল",
        english:"Mrigal",
        temperature:[24,30],
        ph:[6.5,8.5],
        do:5,
        protein:28,
        feed:"পিলেট + প্রাকৃতিক খাদ্য"
    },

    silverCarp:{
        name:"সিলভার কার্প",
        english:"Silver Carp",
        temperature:[22,30],
        ph:[6.5,8.5],
        do:5,
        protein:25,
        feed:"প্রাকৃতিক খাদ্য + পিলেট"
    },

    grassCarp:{
        name:"গ্রাস কার্প",
        english:"Grass Carp",
        temperature:[22,30],
        ph:[6.5,8.5],
        do:5,
        protein:25,
        feed:"উদ্ভিদজাত খাদ্য + পিলেট"
    },

    commonCarp:{
        name:"কমন কার্প",
        english:"Common Carp",
        temperature:[20,30],
        ph:[6.5,8.5],
        do:5,
        protein:28,
        feed:"পিলেট ফিড"
    },

    koi:{
        name:"কৈ",
        english:"Koi",
        temperature:[24,30],
        ph:[6.5,8],
        do:4,
        protein:32,
        feed:"উচ্চ প্রোটিন পিলেট"
    },

    shing:{
        name:"শিং",
        english:"Stinging Catfish",
        temperature:[24,30],
        ph:[6.5,8],
        do:4,
        protein:32,
        feed:"উচ্চ প্রোটিন পিলেট"
    },

    magur:{
        name:"মাগুর",
        english:"Walking Catfish",
        temperature:[24,30],
        ph:[6.5,8],
        do:4,
        protein:32,
        feed:"উচ্চ প্রোটিন পিলেট"
    },

    pabda:{
        name:"পাবদা",
        english:"Pabda",
        temperature:[24,30],
        ph:[6.5,8],
        do:5,
        protein:32,
        feed:"উচ্চ প্রোটিন ফিড"
    },

    gulsha:{
        name:"গুলশা",
        english:"Gulsha",
        temperature:[24,30],
        ph:[6.5,8],
        do:5,
        protein:30,
        feed:"পিলেট ফিড"
    },

    bata:{
        name:"বাটা",
        english:"Bata",
        temperature:[24,30],
        ph:[6.5,8.5],
        do:5,
        protein:28,
        feed:"পিলেট + প্রাকৃতিক খাদ্য"
    },

    vetki:{
        name:"ভেটকি",
        english:"Asian Seabass",
        temperature:[24,30],
        ph:[7,8.5],
        do:5,
        protein:40,
        feed:"উচ্চ প্রোটিন ফিড"
    },

    parshe:{
        name:"পারশে",
        english:"Mullet",
        temperature:[24,30],
        ph:[7,8.5],
        do:5,
        protein:32,
        feed:"পিলেট ফিড"
    },

    pomfret:{
        name:"পমফ্রেট",
        english:"Pomfret",
        temperature:[24,29],
        ph:[7.5,8.5],
        do:5,
        protein:40,
        feed:"উচ্চ প্রোটিন ফিড"
    },

    mola:{
        name:"মলা",
        english:"Mola",
        temperature:[23,30],
        ph:[6.5,8.5],
        do:5,
        protein:30,
        feed:"ক্ষুদ্র পিলেট + প্রাকৃতিক খাদ্য"
    },

    taki:{
        name:"টাকি",
        english:"Spotted Snakehead",
        temperature:[24,30],
        ph:[6.5,8],
        do:4,
        protein:35,
        feed:"উচ্চ প্রোটিন ফিড"
    },

    shol:{
        name:"শোল",
        english:"Snakehead",
        temperature:[24,30],
        ph:[6.5,8],
        do:4,
        protein:35,
        feed:"উচ্চ প্রোটিন ফিড"
    },

    boal:{
        name:"বোয়াল",
        english:"Wallago Catfish",
        temperature:[24,30],
        ph:[6.5,8],
        do:4,
        protein:35,
        feed:"উচ্চ প্রোটিন ফিড"
    }

};


/* =====================================================
   LOAD FISH
===================================================== */

const fishSelect =
document.getElementById("fishSelect");


Object.keys(fishDatabase).forEach(function(key){

    const fish =
    fishDatabase[key];

    const option =
    document.createElement("option");

    option.value=key;

    option.textContent =
    `${fish.name} (${fish.english})`;

    fishSelect.appendChild(option);

});


/* =====================================================
   FISH PROFILE
===================================================== */

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

        box.innerHTML="";

        return;
    }


    const fish =
    fishDatabase[key];


    box.innerHTML=`

        <h3>🐟 ${fish.name}</h3>

        <div class="fish-profile-grid">

            <div class="profile-item">
                <b>তাপমাত্রা</b>
                ${fish.temperature[0]}–${fish.temperature[1]} °C
            </div>

            <div class="profile-item">
                <b>pH</b>
                ${fish.ph[0]}–${fish.ph[1]}
            </div>

            <div class="profile-item">
                <b>DO</b>
                ≥ ${fish.do} mg/L
            </div>

            <div class="profile-item">
                <b>প্রস্তাবিত Protein</b>
                ${fish.protein}%
            </div>

            <div class="profile-item">
                <b>খাদ্য</b>
                ${fish.feed}
            </div>

        </div>
    `;


    box.classList.remove("hidden");
}


/* =====================================================
   MAIN ANALYSIS
===================================================== */

function analyzeCage(){

    const fishKey =
    document.getElementById("fishSelect").value;


    if(!fishKey){

        alert("⚠️ প্রথমে মাছ নির্বাচন করুন।");

        return;
    }


    const fish =
    fishDatabase[fishKey];


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


    if(
        length<=0 ||
        width<=0 ||
        depth<=0 ||
        count<=0 ||
        weight<=0
    ){

        alert(
            "⚠️ খাঁচা ও মাছের প্রয়োজনীয় তথ্য সঠিকভাবে দিন।"
        );

        return;
    }


    /* ================================================
       VOLUME
    ================================================= */

    const volume =
    length * width * depth;


    /* ================================================
       BIOMASS
    ================================================= */

    const biomass =
    (count * weight) / 1000;


    /* ================================================
       DENSITY
    ================================================= */

    const density =
    count / volume;


    /* ================================================
       FEED
    ================================================= */

    let feedRate;


    if(weight < 20){

        feedRate=0.08;

    }else if(weight < 50){

        feedRate=0.06;

    }else if(weight < 100){

        feedRate=0.04;

    }else{

        feedRate=0.03;

    }


    const dailyFeed =
    biomass * 1000 * feedRate;


    /* ================================================
       SHOW CALCULATIONS
    ================================================= */

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


    /* ================================================
       WATER CHECK
    ================================================= */

    const checks=[];


    checks.push(
        waterCheck(
            "🌡️ তাপমাত্রা",
            temperature,
            `${fish.temperature[0]}–${fish.temperature[1]} °C`,
            temperature >= fish.temperature[0] &&
            temperature <= fish.temperature[1]
        )
    );


    checks.push(
        waterCheck(
            "🧪 pH",
            ph,
            `${fish.ph[0]}–${fish.ph[1]}`,
            ph >= fish.ph[0] &&
            ph <= fish.ph[1]
        )
    );


    checks.push(
        waterCheck(
            "💨 DO",
            oxygen,
            `≥ ${fish.do} mg/L`,
            oxygen >= fish.do
        )
    );


    checks.push(
        waterCheck(
            "☠️ Ammonia",
            ammonia,
            "≤ 0.05 mg/L",
            ammonia <= 0.05
        )
    );


    checks.push(
        waterCheck(
            "☠️ Nitrite",
            nitrite,
            "≤ 0.10 mg/L",
            nitrite <= 0.10
        )
    );


    if(transparency>0){

        checks.push(
            waterCheck(
                "💧 স্বচ্ছতা",
                transparency,
                "সাধারণ পর্যবেক্ষণ",
                transparency >= 20
            )
        );

    }


    document.getElementById(
        "waterResults"
    ).innerHTML =
    checks.join("");


    /* ================================================
       PREDICTION
    ================================================= */

    let risk=0;

    let reasons=[];


    if(
        temperature < fish.temperature[0] ||
        temperature > fish.temperature[1]
    ){

        risk+=2;

        reasons.push(
            "তাপমাত্রা অনুকূল নয়"
        );

    }


    if(
        ph < fish.ph[0] ||
        ph > fish.ph[1]
    ){

        risk+=2;

        reasons.push(
            "pH অনুকূল নয়"
        );

    }


    if(oxygen < fish.do){

        risk+=3;

        reasons.push(
            "DO কম"
        );

    }


    if(ammonia > 0.05){

        risk+=3;

        reasons.push(
            "অ্যামোনিয়া বেশি"
        );

    }


    if(nitrite > 0.10){

        risk+=3;

        reasons.push(
            "নাইট্রাইট বেশি"
        );

    }


    if(mortality > 3){

        risk+=3;

        reasons.push(
            "মৃত্যুহার বেশি"
        );

    }


    if(density > 150){

        risk+=2;

        reasons.push(
            "মাছের ঘনত্ব বেশি"
        );

    }


    let prediction;


    if(risk>=7){

        prediction=`

        <div class="prediction danger">

            🚨 <strong>উচ্চ ঝুঁকি</strong>

            <br><br>

            আপনার দেওয়া তথ্য অনুযায়ী মাছের জন্য
            বর্তমানে উল্লেখযোগ্য ঝুঁকি রয়েছে।

            <br><br>

            <strong>সম্ভাব্য কারণ:</strong>
            ${reasons.join(" • ")}

        </div>

        `;

    }

    else if(risk>=3){

        prediction=`

        <div class="prediction warning">

            ⚠️ <strong>মাঝারি ঝুঁকি</strong>

            <br><br>

            কিছু পানির মান ও ব্যবস্থাপনা
            বিষয় দ্রুত পর্যবেক্ষণ করা প্রয়োজন।

            <br><br>

            ${reasons.length
                ? reasons.join(" • ")
                : "নিয়মিত পর্যবেক্ষণ চালিয়ে যান।"
            }

        </div>

        `;

    }

    else{

        prediction=`

        <div class="prediction good">

            ✅ <strong>বর্তমান অবস্থা ভালো</strong>

            <br><br>

            আপনার দেওয়া তথ্য অনুযায়ী
            প্রধান পরিবেশগত সূচকগুলো
            নির্বাচিত মাছের জন্য গ্রহণযোগ্য।

            <br><br>

            নিয়মিত পানি পরীক্ষা ও
            মাছের আচরণ পর্যবেক্ষণ করুন।

        </div>

        `;

    }


    document.getElementById(
        "predictionBox"
    ).innerHTML=prediction;


    /* ================================================
       FARMER ADVICE
    ================================================= */

    const advice=[];


    advice.push(
        "প্রতিদিন সকাল ও বিকেলে মাছের আচরণ এবং খাবার গ্রহণ পর্যবেক্ষণ করুন।"
    );


    advice.push(
        "খাঁচার জাল নিয়মিত পরিষ্কার রাখুন যাতে পানির প্রবাহ বাধাগ্রস্ত না হয়।"
    );


    advice.push(
        "খাবার অতিরিক্ত দেবেন না; অবশিষ্ট খাবার পানিতে জমতে দেওয়া উচিত নয়।"
    );


    advice.push(
        "DO, pH, temperature, ammonia এবং nitrite নিয়মিত পরীক্ষা করুন।"
    );


    if(oxygen < fish.do){

        advice.push(
            "🚨 DO কম — পানির প্রবাহ/বায়ু চলাচল বাড়ানোর ব্যবস্থা করুন এবং কারণ অনুসন্ধান করুন।"
        );

    }


    if(ammonia > 0.05){

        advice.push(
            "🚨 Ammonia বেশি — অতিরিক্ত feed ও জৈব বর্জ্য নিয়ন্ত্রণ করুন এবং পানির মান দ্রুত পুনরায় পরীক্ষা করুন।"
        );

    }


    if(nitrite > 0.10){

        advice.push(
            "🚨 Nitrite বেশি — পানির গুণমান ও বর্জ্য ব্যবস্থাপনা পরীক্ষা করুন।"
        );

    }


    if(mortality > 3){

        advice.push(
            "🚨 মৃত্যুহার বেশি হলে মৃত মাছ দ্রুত সরিয়ে মাছের রোগের লক্ষণ ও পানির মান পরীক্ষা করুন।"
        );

    }


    advice.push(
        `এই মাছের জন্য সাধারণভাবে ${fish.protein}% এর কাছাকাছি protein feed উপযোগী হতে পারে; মাছের বয়স ও উৎপাদন পর্যায় অনুযায়ী feed নির্বাচন করুন।`
    );


    document.getElementById(
        "adviceList"
    ).innerHTML =
    advice.map(function(text){

        return `
            <div class="advice-item">
                <span class="advice-icon">💡</span>
                <span>${text}</span>
            </div>
        `;

    }).join("");


    /* ================================================
       SHOW RESULT
    ================================================= */

    document.getElementById(
        "resultSection"
    ).classList.remove("hidden");


    document.getElementById(
        "resultSection"
    ).scrollIntoView({
        behavior:"smooth"
    });

}


/* =====================================================
   NUMBER HELPER
===================================================== */

function getNumber(id){

    const value =
    parseFloat(
        document.getElementById(id).value
    );

    return Number.isFinite(value)
        ? value
        : 0;
}


/* =====================================================
   WATER RESULT HTML
===================================================== */

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

            <h3>${title}</h3>

            <strong>
                ${value}
            </strong>

            <br>

            আদর্শ:
            ${ideal}

            <br>

            <strong>
                ${status}
            </strong>

        </div>

    `;
}


/* =====================================================
   BACK
===================================================== */


function goBack() {

    if (
        document.referrer &&
        document.referrer !== window.location.href
    ) {

        history.back();

    } else {

        window.location.href = "cage_culture.html";

    }

}