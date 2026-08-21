const imageInput =
    document.getElementById("imageInput");

const previewBox =
    document.getElementById("previewBox");

const previewImage =
    document.getElementById("previewImage");

const analyzeBtn =
    document.getElementById("analyzeBtn");

const loadingBox =
    document.getElementById("loadingBox");

const resultBox =
    document.getElementById("resultBox");

const resultContent =
    document.getElementById("resultContent");


let selectedFile = null;


imageInput.addEventListener(
    "change",
    function () {

        const file =
            this.files[0];


        if (!file) {

            return;
        }


        selectedFile = file;


        const reader =
            new FileReader();


        reader.onload =
            function (event) {

                previewImage.src =
                    event.target.result;


                previewBox.style.display =
                    "block";


                analyzeBtn.disabled =
                    false;
            };


        reader.readAsDataURL(file);

    }
);


// ------------------------------------------------
// ANALYZE
// ------------------------------------------------

analyzeBtn.addEventListener(
    "click",
    async function () {

        if (!selectedFile) {

            alert(
                "আগে একটি ছবি নির্বাচন করুন।"
            );

            return;
        }


        loadingBox.style.display =
            "block";


        resultBox.style.display =
            "none";


        analyzeBtn.disabled =
            true;


        const formData =
            new FormData();


        formData.append(
            "image",
            selectedFile
        );


        try {

            const response =
                await fetch(
                "/predict-disease",
                {
                    method: "POST",
                    body: formData
                }
            );


            const data =
                await response.json();


            loadingBox.style.display =
                "none";


            resultBox.style.display =
                "block";


            if (!data.success) {

                resultContent.innerHTML = `

                    <div class="error">

                        ❌ ${data.message}

                    </div>

                `;

                return;
            }


            const confidence =
                data.confidence;


            let confidenceText =
                "";


            if (confidence >= 85) {

                confidenceText =
                    "উচ্চ confidence";

            }

            else if (confidence >= 60) {

                confidenceText =
                    "মাঝারি confidence";

            }

            else {

                confidenceText =
                    "কম confidence";
            }


const info = data.information;

if (!info) {

    resultContent.innerHTML = `

        <div class="diagnosis-card">

            <h3>🌱 রোগ শনাক্ত হয়েছে</h3>

            <div class="disease-name">
                ${data.disease}
            </div>

            <p>
                Confidence:
                <strong>
                    ${data.confidence}%
                </strong>
            </p>

            <div class="warning">
                এই রোগের বিস্তারিত তথ্য
                এখনো database-এ যোগ করা হয়নি।
            </div>

        </div>

    `;

    return;
}


resultContent.innerHTML = `

<div class="diagnosis-card">

    <h3>🌱 ফসল</h3>

    <div class="disease-name">
        ${info.crop_bn}
    </div>


    <h3>🦠 রোগ</h3>

    <div class="disease-name">
        ${info.disease_bn}
    </div>


    <p>
        <strong>AI Confidence:</strong>
        ${data.confidence}%
    </p>


    <hr>


    <h3>🔍 রোগের লক্ষণ</h3>

    <p>
        ${info.symptoms}
    </p>


    <h3>🦠 রোগের কারণ</h3>

    <p>
        ${info.scientific_cause}
    </p>


    <h3>🌦️ অনুকূল পরিবেশ</h3>

    <p>
        ${info.favorable_condition}
    </p>


    <h3>🛡️ প্রতিরোধ</h3>

    <p>
        ${info.prevention}
    </p>


    <h3>🛠️ ব্যবস্থাপনা</h3>

    <p>
        ${info.management}
    </p>


    <h3>💊 চিকিৎসা</h3>

    <p>
        ${info.medicine || "তথ্য যাচাই করে যোগ করা হবে।"}
    </p>


    <h3>📋 প্রয়োগ পদ্ধতি</h3>

    <p>
        ${info.application || "তথ্য যাচাই করে যোগ করা হবে।"}
    </p>


    <h3>⚠️ সতর্কতা</h3>

    <p>
        ${info.safety || "অনুমোদিত label অনুসরণ করুন।"}
    </p>


    <hr>


    <p>
        📚 তথ্যের উৎস:
        ${info.source}
    </p>

</div>

`;


    } catch (error) {

            console.error(error);


            loadingBox.style.display =
                "none";


            resultBox.style.display =
                "block";


            resultContent.innerHTML = `

                <div class="error">

                    ❌ Server-এর সাথে
                    যোগাযোগ করা যাচ্ছে না।

                </div>

            `;

        }


        finally {

            analyzeBtn.disabled =
                false;

        }

    }
);
