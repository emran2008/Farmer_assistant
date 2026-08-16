/* =========================================================
   RAS FISH FARMING SYSTEM
   ========================================================= */


/* =========================================================
   ৫০টি প্রচলিত মাছের ডাটাবেস
   ========================================================= */

const fishDatabase = [

    {
        name: "তেলাপিয়া",
        en: "Tilapia",
        temp: [25, 30],
        ph: [6.5, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 10,
        hardness: [50, 200],
        feedProtein: "28-35%",
        stocking: "মাঝারি-উচ্চ"
    },

    {
        name: "নাইল তেলাপিয়া",
        en: "Nile Tilapia",
        temp: [25, 30],
        ph: [6.5, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 15,
        hardness: [50, 200],
        feedProtein: "28-35%",
        stocking: "উচ্চ"
    },

    {
        name: "রুই",
        en: "Rohu",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "কাতলা",
        en: "Catla",
        temp: [25, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "মৃগেল",
        en: "Mrigal",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "কালিবাউশ",
        en: "Black Rohu",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "পাঙ্গাস",
        en: "Pangasius",
        temp: [26, 30],
        ph: [6.5, 8],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 250],
        feedProtein: "28-32%",
        stocking: "উচ্চ"
    },

    {
        name: "শিং",
        en: "Walking Catfish",
        temp: [25, 30],
        ph: [6.5, 8],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 250],
        feedProtein: "32-38%",
        stocking: "উচ্চ"
    },

    {
        name: "মাগুর",
        en: "Magur",
        temp: [25, 30],
        ph: [6.5, 8],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 250],
        feedProtein: "32-38%",
        stocking: "উচ্চ"
    },

    {
        name: "কৈ",
        en: "Koi",
        temp: [24, 30],
        ph: [6.5, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 250],
        feedProtein: "30-35%",
        stocking: "উচ্চ"
    },

    {
        name: "শোল",
        en: "Snakehead",
        temp: [24, 30],
        ph: [6.5, 8.5],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 250],
        feedProtein: "35-40%",
        stocking: "মাঝারি"
    },

    {
        name: "টাকি",
        en: "Spotted Snakehead",
        temp: [24, 30],
        ph: [6.5, 8.5],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 250],
        feedProtein: "32-38%",
        stocking: "মাঝারি"
    },

    {
        name: "বোয়াল",
        en: "Wallago",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 2,
        hardness: [50, 200],
        feedProtein: "35-40%",
        stocking: "কম"
    },

    {
        name: "আইড়",
        en: "Aor",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 2,
        hardness: [50, 200],
        feedProtein: "35-40%",
        stocking: "কম"
    },

    {
        name: "পাবদা",
        en: "Pabda",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "32-38%",
        stocking: "মাঝারি"
    },

    {
        name: "গুলশা",
        en: "Gulsha",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "32-38%",
        stocking: "মাঝারি"
    },

    {
        name: "টেংরা",
        en: "Tengra",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "30-35%",
        stocking: "মাঝারি"
    },

    {
        name: "বাটা",
        en: "Bata",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "সরপুঁটি",
        en: "Sharpunti",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "পুঁটি",
        en: "Punti",
        temp: [23, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "মলা",
        en: "Mola",
        temp: [23, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "বেলে",
        en: "Bele",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "30-35%",
        stocking: "মাঝারি"
    },

    {
        name: "চিংড়ি",
        en: "Freshwater Prawn",
        temp: [26, 30],
        ph: [7, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 10,
        hardness: [100, 300],
        feedProtein: "30-35%",
        stocking: "মাঝারি"
    },

    {
        name: "গলদা চিংড়ি",
        en: "Giant Freshwater Prawn",
        temp: [26, 31],
        ph: [7, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [100, 300],
        feedProtein: "30-35%",
        stocking: "মাঝারি"
    },

    {
        name: "গ্রাস কার্প",
        en: "Grass Carp",
        temp: [20, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "সিলভার কার্প",
        en: "Silver Carp",
        temp: [20, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "বিগহেড কার্প",
        en: "Bighead Carp",
        temp: [20, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "কমন কার্প",
        en: "Common Carp",
        temp: [20, 30],
        ph: [6.5, 8.5],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 300],
        feedProtein: "25-30%",
        stocking: "উচ্চ"
    },

    {
        name: "মিরর কার্প",
        en: "Mirror Carp",
        temp: [20, 30],
        ph: [6.5, 8.5],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 300],
        feedProtein: "25-30%",
        stocking: "উচ্চ"
    },

    {
        name: "কই কার্প",
        en: "Koi Carp",
        temp: [20, 30],
        ph: [6.5, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 300],
        feedProtein: "30-35%",
        stocking: "উচ্চ"
    },

    {
        name: "পাইক কার্প",
        en: "Common Pike",
        temp: [18, 28],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 2,
        hardness: [50, 200],
        feedProtein: "30-35%",
        stocking: "কম"
    },

    {
        name: "ব্ল্যাক কার্প",
        en: "Black Carp",
        temp: [20, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "28-32%",
        stocking: "মাঝারি"
    },

    {
        name: "মাহশের",
        en: "Mahseer",
        temp: [18, 26],
        ph: [6.5, 8],
        do: 6,
        ammonia: 0.02,
        nitrite: 0.2,
        salinity: 1,
        hardness: [50, 200],
        feedProtein: "30-35%",
        stocking: "কম"
    },

    {
        name: "ট্রাউট",
        en: "Rainbow Trout",
        temp: [10, 18],
        ph: [6.5, 8],
        do: 7,
        ammonia: 0.02,
        nitrite: 0.2,
        salinity: 5,
        hardness: [50, 200],
        feedProtein: "38-45%",
        stocking: "উচ্চ"
    },

    {
        name: "সালমন",
        en: "Salmon",
        temp: [10, 18],
        ph: [6.5, 8],
        do: 7,
        ammonia: 0.02,
        nitrite: 0.2,
        salinity: 35,
        hardness: [50, 200],
        feedProtein: "40-45%",
        stocking: "উচ্চ"
    },

    {
        name: "বাস",
        en: "Asian Sea Bass",
        temp: [26, 30],
        ph: [7, 8.5],
        do: 5,
        ammonia: 0.02,
        nitrite: 0.2,
        salinity: 30,
        hardness: [100, 300],
        feedProtein: "40-45%",
        stocking: "উচ্চ"
    },

    {
        name: "কোরাল",
        en: "Coral Fish",
        temp: [25, 30],
        ph: [7.5, 8.5],
        do: 5,
        ammonia: 0.02,
        nitrite: 0.2,
        salinity: 30,
        hardness: [100, 300],
        feedProtein: "40-45%",
        stocking: "মাঝারি"
    },

    {
        name: "মুলেট",
        en: "Mullet",
        temp: [20, 30],
        ph: [7, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 25,
        hardness: [100, 300],
        feedProtein: "28-35%",
        stocking: "মাঝারি"
    },

    {
        name: "ভেটকি",
        en: "Barramundi",
        temp: [26, 30],
        ph: [7, 8.5],
        do: 5,
        ammonia: 0.02,
        nitrite: 0.2,
        salinity: 20,
        hardness: [100, 300],
        feedProtein: "40-45%",
        stocking: "উচ্চ"
    },

    {
        name: "কাকিলা",
        en: "Freshwater Garfish",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "30-35%",
        stocking: "মাঝারি"
    },

    {
        name: "চান্দা",
        en: "Chanda",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "30-35%",
        stocking: "মাঝারি"
    },

    {
        name: "চেলা",
        en: "Chela",
        temp: [23, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "28-32%",
        stocking: "মাঝারি"
    },

    {
        name: "কৈ মাছ",
        en: "Climbing Perch",
        temp: [24, 30],
        ph: [6.5, 8.5],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 250],
        feedProtein: "30-35%",
        stocking: "উচ্চ"
    },

    {
        name: "তিত পুঁটি",
        en: "Tite Punti",
        temp: [23, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    },

    {
        name: "মেনি",
        en: "Meni",
        temp: [23, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "28-32%",
        stocking: "মাঝারি"
    },

    {
        name: "বাইম",
        en: "Spiny Eel",
        temp: [24, 30],
        ph: [6.5, 8],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "32-38%",
        stocking: "কম"
    },

    {
        name: "চিংড়ি বাগদা",
        en: "Black Tiger Shrimp",
        temp: [26, 31],
        ph: [7.5, 8.5],
        do: 5,
        ammonia: 0.02,
        nitrite: 0.2,
        salinity: 25,
        hardness: [100, 300],
        feedProtein: "35-40%",
        stocking: "উচ্চ"
    },

    {
        name: "গলদা",
        en: "Macrobrachium",
        temp: [26, 31],
        ph: [7, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [100, 300],
        feedProtein: "30-35%",
        stocking: "মাঝারি"
    },

    {
        name: "তেলাপিয়া রেড",
        en: "Red Tilapia",
        temp: [25, 30],
        ph: [6.5, 8.5],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 10,
        hardness: [50, 200],
        feedProtein: "28-35%",
        stocking: "উচ্চ"
    },

    {
        name: "পাঙ্গাসী",
        en: "Pangasius Hybrid",
        temp: [26, 30],
        ph: [6.5, 8],
        do: 4,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 5,
        hardness: [50, 250],
        feedProtein: "28-32%",
        stocking: "উচ্চ"
    },

    {
        name: "গ্রাস কার্প",
        en: "Grass Carp",
        temp: [20, 30],
        ph: [6.5, 8],
        do: 5,
        ammonia: 0.05,
        nitrite: 0.5,
        salinity: 3,
        hardness: [50, 200],
        feedProtein: "25-30%",
        stocking: "মাঝারি"
    }

];


/* =========================================================
   INITIALIZE
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {

    const fishSelect =
        document.getElementById("fishSelect");

    if (!fishSelect) return;


    fishDatabase.forEach((fish, index) => {

        const option =
            document.createElement("option");

        option.value = index;

        option.textContent =
            `${fish.name} (${fish.en})`;

        fishSelect.appendChild(option);

    });


    fishSelect.addEventListener(
        "change",
        showFishInfo
    );

});


/* =========================================================
   SHOW FISH INFORMATION
   ========================================================= */

function showFishInfo() {

    const value =
        document.getElementById("fishSelect").value;

    const box =
        document.getElementById("fishInfo");


    if (value === "") {

        box.classList.add("hidden");

        box.innerHTML = "";

        return;
    }


    const fish =
        fishDatabase[Number(value)];


    box.classList.remove("hidden");


    box.innerHTML = `

        <h3>🐟 ${fish.name} — ${fish.en}</h3>

        <p>
            এই মাছের জন্য প্রস্তাবিত RAS পানি ও ব্যবস্থাপনার
            সাধারণ রেঞ্জ:
        </p>

        <div class="fish-parameter-grid">

            <div class="parameter">
                <strong>Temperature</strong>
                ${fish.temp[0]}–${fish.temp[1]} °C
            </div>

            <div class="parameter">
                <strong>pH</strong>
                ${fish.ph[0]}–${fish.ph[1]}
            </div>

            <div class="parameter">
                <strong>DO</strong>
                ≥ ${fish.do} mg/L
            </div>

            <div class="parameter">
                <strong>Ammonia</strong>
                ≤ ${fish.ammonia} mg/L
            </div>

            <div class="parameter">
                <strong>Nitrite</strong>
                ≤ ${fish.nitrite} mg/L
            </div>

            <div class="parameter">
                <strong>Hardness</strong>
                ${fish.hardness[0]}–${fish.hardness[1]}
            </div>

            <div class="parameter">
                <strong>Salinity</strong>
                ≤ ${fish.salinity} ppt
            </div>

            <div class="parameter">
                <strong>Feed Protein</strong>
                ${fish.feedProtein}
            </div>

        </div>
    `;
}


/* =========================================================
   READ NUMBER
   ========================================================= */

function numberValue(id) {

    const el =
        document.getElementById(id);

    if (!el || el.value === "") {
        return null;
    }

    return Number(el.value);
}


/* =========================================================
   MAIN ANALYSIS
   ========================================================= */

function analyzeRAS() {

    const fishIndex =
        document.getElementById("fishSelect").value;


    if (fishIndex === "") {

        alert("প্রথমে মাছ নির্বাচন করুন।");

        return;
    }


    const fish =
        fishDatabase[Number(fishIndex)];


    const temperature =
        numberValue("temperature");

    const ph =
        numberValue("ph");

    const doValue =
        numberValue("doValue");

    const ammonia =
        numberValue("ammonia");

    const nitrite =
        numberValue("nitrite");

    const alkalinity =
        numberValue("alkalinity");

    const hardness =
        numberValue("hardness");

    const salinity =
        numberValue("salinity");


    const tankVolume =
        numberValue("tankVolume");

    const waterFlow =
        numberValue("waterFlow");

    const fishCount =
        numberValue("fishCount");

    const fishWeight =
        numberValue("fishWeight");


    const deadFish =
        numberValue("deadFish") || 0;


    const appetite =
        document.getElementById("appetite").value;


    const aeration =
        document.getElementById("aeration").value;


    const biofilter =
        document.getElementById("biofilter").value;


    const mechanicalFilter =
        document.getElementById("mechanicalFilter").value;


    const uv =
        document.getElementById("uv").value;


    const otherSymptoms =
        document
        .getElementById("otherSymptoms")
        .value
        .toLowerCase();


    const checkedSymptoms =
        Array.from(
            document.querySelectorAll(
                ".symptoms-grid input:checked"
            )
        ).map(
            input => input.value
        );


    let waterProblems = [];

    let waterScore = 0;


    /* TEMPERATURE */

    if (temperature !== null) {

        if (
            temperature < fish.temp[0] ||
            temperature > fish.temp[1]
        ) {

            waterScore += 2;

            waterProblems.push(
                `Temperature ${temperature}°C — মাছের প্রস্তাবিত ${fish.temp[0]}–${fish.temp[1]}°C`
            );
        }
    }


    /* PH */

    if (ph !== null) {

        if (
            ph < fish.ph[0] ||
            ph > fish.ph[1]
        ) {

            waterScore += 2;

            waterProblems.push(
                `pH ${ph} — প্রস্তাবিত ${fish.ph[0]}–${fish.ph[1]}`
            );
        }
    }


    /* DO */

    if (doValue !== null) {

        if (doValue < fish.do) {

            waterScore += 3;

            waterProblems.push(
                `DO মাত্রা কম (${doValue} mg/L)`
            );
        }
    }


    /* AMMONIA */

    if (ammonia !== null) {

        if (ammonia > fish.ammonia) {

            waterScore += 4;

            waterProblems.push(
                `Ammonia বেশি (${ammonia} mg/L)`
            );
        }
    }


    /* NITRITE */

    if (nitrite !== null) {

        if (nitrite > fish.nitrite) {

            waterScore += 4;

            waterProblems.push(
                `Nitrite বেশি (${nitrite} mg/L)`
            );
        }
    }


    /* HARDNESS */

    if (hardness !== null) {

        if (
            hardness < fish.hardness[0] ||
            hardness > fish.hardness[1]
        ) {

            waterScore += 1;

            waterProblems.push(
                `Hardness ${hardness} mg/L — সাধারণ রেঞ্জের বাইরে`
            );
        }
    }


    /* SALINITY */

    if (salinity !== null) {

        if (salinity > fish.salinity) {

            waterScore += 2;

            waterProblems.push(
                `Salinity ${salinity} ppt — এই মাছের জন্য বেশি হতে পারে`
            );
        }
    }


    /* ALKALINITY */

    if (alkalinity !== null) {

        if (alkalinity < 60) {

            waterScore += 2;

            waterProblems.push(
                `Alkalinity কম (${alkalinity} mg/L)`
            );
        }
    }


    /* =====================================================
       DISEASE / PROBLEM PREDICTION
       ===================================================== */

    let predictions = [];


    function has(symptom) {

        return checkedSymptoms.includes(symptom);
    }


    /* LOW OXYGEN */

    if (
        has("surface") ||
        has("balance") ||
        (doValue !== null && doValue < fish.do)
    ) {

        predictions.push({

            title: "🫧 Low Dissolved Oxygen / Oxygen Stress",

            probability: "উচ্চ",

            reason:
                "মাছ পানির উপরে উঠে হাঁসফাঁস করা বা DO কম থাকা অক্সিজেন সমস্যার সাথে সামঞ্জস্যপূর্ণ।",

            action: [
                "Aeration বাড়ান",
                "Air blower / diffuser পরীক্ষা করুন",
                "মৃত ও অতিরিক্ত জৈব পদার্থ সরান",
                "খাবার সাময়িকভাবে কমিয়ে পানির মান পর্যবেক্ষণ করুন"
            ]

        });

    }


    /* AMMONIA */

    if (
        ammonia !== null &&
        ammonia > fish.ammonia
    ) {

        predictions.push({

            title: "☠️ Ammonia Stress / Toxicity Risk",

            probability: "উচ্চ",

            reason:
                "RAS পানিতে Ammonia মাছের জন্য ক্ষতিকর মাত্রায় রয়েছে।",

            action: [
                "Feed কমান",
                "Biofilter কার্যক্ষমতা পরীক্ষা করুন",
                "Mechanical filter পরিষ্কার করুন",
                "পানির Ammonia পুনরায় পরীক্ষা করুন",
                "Aeration বজায় রাখুন"
            ]

        });

    }


    /* NITRITE */

    if (
        nitrite !== null &&
        nitrite > fish.nitrite
    ) {

        predictions.push({

            title: "☠️ Nitrite Stress",

            probability: "উচ্চ",

            reason:
                "Nitrite বৃদ্ধি Biofilter / nitrification সমস্যার ইঙ্গিত দিতে পারে।",

            action: [
                "Biofilter পরীক্ষা করুন",
                "অতিরিক্ত feed বন্ধ/কম করুন",
                "পানি পরীক্ষার frequency বাড়ান",
                "Aeration ঠিক রাখুন"
            ]

        });

    }


    /* ICH */

    if (
        has("white_spots")
    ) {

        predictions.push({

            title: "⚪ সম্ভাব্য Ich / White Spot সমস্যা",

            probability: "মাঝারি-উচ্চ",

            reason:
                "শরীরে সাদা দাগ Ich জাতীয় parasitic problem-এর সাথে সামঞ্জস্যপূর্ণ হতে পারে।",

            action: [
                "আক্রান্ত মাছ আলাদা করুন",
                "নতুন মাছ quarantine করুন",
                "পানির মান স্থিতিশীল রাখুন",
                "বিশেষজ্ঞের মাধ্যমে রোগ নিশ্চিত করুন"
            ]

        });

    }


    /* BACTERIAL */

    if (
        has("red_spots") ||
        has("ulcer") ||
        has("eye")
    ) {

        predictions.push({

            title: "🔴 সম্ভাব্য Bacterial Disease / Septicemia",

            probability: "মাঝারি-উচ্চ",

            reason:
                "লাল দাগ, ulcer বা চোখ ফুলে যাওয়ার মতো লক্ষণ bacterial infection-এর সাথে সম্পর্কিত হতে পারে।",

            action: [
                "আক্রান্ত মাছ আলাদা করুন",
                "পানির মান ঠিক করুন",
                "Dead fish দ্রুত সরান",
                "অ্যান্টিবায়োটিক নিজে থেকে ব্যবহার করবেন না",
                "বিশেষজ্ঞের মাধ্যমে রোগ নিশ্চিত করুন"
            ]

        });

    }


    /* FUNGAL */

    if (
        has("cotton")
    ) {

        predictions.push({

            title: "🍄 সম্ভাব্য Fungal Infection",

            probability: "মাঝারি",

            reason:
                "তুলার মতো সাদা বৃদ্ধি fungal infection-এর সাথে সামঞ্জস্যপূর্ণ হতে পারে।",

            action: [
                "আক্রান্ত মাছ আলাদা করুন",
                "পানির মান উন্নত করুন",
                "মৃত মাছ ও জৈব বর্জ্য সরান",
                "বিশেষজ্ঞের পরামর্শ নিন"
            ]

        });

    }


    /* FIN ROT */

    if (
        has("fin_rot")
    ) {

        predictions.push({

            title: "🦠 সম্ভাব্য Fin Rot",

            probability: "মাঝারি",

            reason:
                "পাখনা ক্ষয় বা পচন bacterial/environmental stress-এর সাথে সম্পর্কিত হতে পারে।",

            action: [
                "পানির Ammonia ও Nitrite পরীক্ষা করুন",
                "Mechanical filter পরিষ্কার করুন",
                "পানির মান স্থিতিশীল রাখুন",
                "আক্রান্ত মাছ পর্যবেক্ষণ করুন"
            ]

        });

    }


    /* PARASITE */

    if (
        has("flashing") ||
        has("mucus")
    ) {

        predictions.push({

            title: "🪱 সম্ভাব্য External Parasite",

            probability: "মাঝারি",

            reason:
                "শরীর ঘষা এবং অতিরিক্ত mucus external parasite-এর সাথে সামঞ্জস্যপূর্ণ হতে পারে।",

            action: [
                "আক্রান্ত মাছ আলাদা করুন",
                "পানির গুণমান পরীক্ষা করুন",
                "Gill ও skin পরীক্ষা করান",
                "বিশেষজ্ঞের পরামর্শ নিন"
            ]

        });

    }


    /* APPETITE */

    if (
        appetite === "none" ||
        appetite === "low"
    ) {

        predictions.push({

            title: "🍽️ Feed Intake Problem",

            probability: "মাঝারি",

            reason:
                "খাবার কম খাওয়া পানি, stress, disease বা feed quality সমস্যার সাথে সম্পর্কিত হতে পারে।",

            action: [
                "পানির Temperature ও DO পরীক্ষা করুন",
                "Ammonia/Nitrite পরীক্ষা করুন",
                "অতিরিক্ত খাবার দেবেন না",
                "মাছের আচরণ পর্যবেক্ষণ করুন"
            ]

        });

    }


    /* MORTALITY */

    if (deadFish > 0) {

        predictions.push({

            title: "💀 Mortality Detected",

            probability:
                deadFish >= 10 ? "উচ্চ" : "মাঝারি",

            reason:
                `গত ২৪ ঘণ্টায় ${deadFish}টি মাছ মারা গেছে। কারণ দ্রুত অনুসন্ধান করা প্রয়োজন।`,

            action: [
                "মৃত মাছ দ্রুত সরান",
                "পানি পরীক্ষা করুন",
                "Aeration পরীক্ষা করুন",
                "Ammonia/Nitrite পরীক্ষা করুন",
                "বিশেষজ্ঞের সাহায্য নিন যদি মৃত্যু বাড়তে থাকে"
            ]

        });

    }


    /* =====================================================
       SYSTEM CHECK
       ===================================================== */

    let systemProblems = [];


    if (biofilter === "no") {

        systemProblems.push(
            "Biofilter নেই — RAS-এর nitrification ব্যবস্থা নিশ্চিত করুন।"
        );

    }


    if (mechanicalFilter === "no") {

        systemProblems.push(
            "Mechanical filter নেই — solids removal ব্যবস্থা উন্নত করুন।"
        );

    }


    if (aeration === "weak") {

        systemProblems.push(
            "Aeration দুর্বল — DO পর্যবেক্ষণ ও aeration capacity বাড়ানো দরকার হতে পারে।"
        );

    }


    if (
        tankVolume &&
        fishCount &&
        fishWeight
    ) {

        const biomassKg =
            (fishCount * fishWeight) / 1000;


        const biomassPer1000L =
            biomassKg / (tankVolume / 1000);


        if (biomassPer1000L > 30) {

            systemProblems.push(
                `Estimated biomass প্রায় ${biomassPer1000L.toFixed(1)} kg/1000L — stocking density বেশি হতে পারে।`
            );

        }

    }


    /* =====================================================
       RISK
       ===================================================== */

    let totalScore =
        waterScore +
        predictions.length;


    let risk =
        "কম";

    if (totalScore >= 7) {

        risk = "উচ্চ";

    } else if (totalScore >= 3) {

        risk = "মাঝারি";

    }


    /* =====================================================
       DISPLAY
       ===================================================== */

    document
        .getElementById("resultSection")
        .classList.remove("hidden");


    const badge =
        document.getElementById("riskBadge");


    badge.textContent =
        `Overall Risk: ${risk}`;


    badge.style.background =
        risk === "উচ্চ"
            ? "#ffe0e0"
            : risk === "মাঝারি"
                ? "#fff0cc"
                : "#dff5e7";


    /* WATER RESULT */

    let waterHTML = `

        <div class="result-box
            ${waterProblems.length ? "warning" : ""}">

            <h3>💧 পানির বিশ্লেষণ</h3>
    `;


    if (waterProblems.length === 0) {

        waterHTML += `
            <p>
                দেওয়া পানির তথ্য অনুযায়ী
                বড় কোনো parameter warning পাওয়া যায়নি।
            </p>
        `;

    } else {

        waterHTML += `
            <ul>
                ${waterProblems
                    .map(problem => `<li>${problem}</li>`)
                    .join("")}
            </ul>
        `;

    }


    waterHTML += `</div>`;


    document.getElementById(
        "waterResult"
    ).innerHTML = waterHTML;


    /* DISEASE RESULT */

    let diseaseHTML = `

        <div class="result-box">

            <h3>🦠 সম্ভাব্য সমস্যা / Prediction</h3>
    `;


    if (predictions.length === 0) {

        diseaseHTML += `

            <p>
                নির্বাচিত লক্ষণের ভিত্তিতে
                নির্দিষ্ট কোনো বড় সম্ভাব্য সমস্যা পাওয়া যায়নি।
            </p>

            <p>
                তবে মাছের আচরণ ও পানির মান নিয়মিত পর্যবেক্ষণ করুন।
            </p>

        `;

    } else {

        predictions.forEach(prediction => {

            diseaseHTML += `

                <div class="result-box warning">

                    <h3>
                        ${prediction.title}
                    </h3>

                    <p>
                        <strong>
                            সম্ভাব্যতা:
                        </strong>

                        ${prediction.probability}
                    </p>

                    <p>
                        ${prediction.reason}
                    </p>

                    <br>

                    <strong>
                        করণীয়:
                    </strong>

                    <ul>

                        ${prediction.action
                            .map(
                                item =>
                                    `<li>${item}</li>`
                            )
                            .join("")}

                    </ul>

                </div>

            `;

        });

    }


    diseaseHTML += `</div>`;


    document.getElementById(
        "diseaseResult"
    ).innerHTML = diseaseHTML;


    /* SYSTEM */

    let systemHTML = `

        <div class="result-box">

            <h3>🔄 RAS System Check</h3>

    `;


    if (systemProblems.length === 0) {

        systemHTML += `

            <p>
                দেওয়া তথ্য অনুযায়ী বড় কোনো
                RAS equipment warning পাওয়া যায়নি।
            </p>

        `;

    } else {

        systemHTML += `

            <ul>

                ${systemProblems
                    .map(
                        problem =>
                            `<li>${problem}</li>`
                    )
                    .join("")}

            </ul>

        `;

    }


    systemHTML += `</div>`;


    document.getElementById(
        "systemResult"
    ).innerHTML = systemHTML;


    /* RECOMMENDATION */

    let recommendation = [];


    if (waterProblems.length > 0) {

        recommendation.push(
            "প্রথমে পানির সমস্যাগুলো ঠিক করুন।"
        );

    }


    if (
        ammonia !== null &&
        ammonia > fish.ammonia
    ) {

        recommendation.push(
            "Feed কমিয়ে Biofilter ও water quality পরীক্ষা করুন।"
        );

    }


    if (
        nitrite !== null &&
        nitrite > fish.nitrite
    ) {

        recommendation.push(
            "Nitrification/Biofilter system পরীক্ষা করুন।"
        );

    }


    if (
        doValue !== null &&
        doValue < fish.do
    ) {

        recommendation.push(
            "Aeration বাড়িয়ে DO নিরাপদ পর্যায়ে রাখার চেষ্টা করুন।"
        );

    }


    if (deadFish > 0) {

        recommendation.push(
            "মৃত মাছ দ্রুত সরিয়ে কারণ অনুসন্ধান করুন।"
        );

    }


    if (predictions.length === 0) {

        recommendation.push(
            "বর্তমানে দেওয়া তথ্য অনুযায়ী নিয়মিত monitoring চালিয়ে যান।"
        );

    }


    document.getElementById(
        "recommendationResult"
    ).innerHTML = `

        <div class="result-box">

            <h3>💡 গুরুত্বপূর্ণ করণীয়</h3>

            <ul>

                ${recommendation
                    .map(
                        item =>
                            `<li>${item}</li>`
                    )
                    .join("")}

            </ul>

        </div>

    `;


    /* SCROLL RESULT */

    document
        .getElementById("resultSection")
        .scrollIntoView({
            behavior: "smooth"
        });

}


/* =========================================================
   RESET
   ========================================================= */

function resetRAS() {

    document
        .querySelectorAll("input")
        .forEach(input => {

            if (input.type === "checkbox") {

                input.checked = false;

            } else {

                input.value = "";

            }

        });


    document
        .querySelectorAll("select")
        .forEach(select => {

            select.selectedIndex = 0;

        });


    document
        .querySelectorAll("textarea")
        .forEach(textarea => {

            textarea.value = "";

        });


    document
        .getElementById("fishInfo")
        .classList.add("hidden");


    document
        .getElementById("resultSection")
        .classList.add("hidden");


    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });

}


/* =========================================================
   BACK
   ========================================================= */

function goBack() {

    if (
        document.referrer &&
        document.referrer !== window.location.href
    ) {

        history.back();

    } else {

        window.location.href = "ras.html";

    }

}