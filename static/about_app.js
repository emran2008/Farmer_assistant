/* ==========================================
   FARMER ASSISTANT
   ABOUT THE APP
========================================== */


/* ==========================================
   TOGGLE INFORMATION CARD
========================================== */

function toggleCard(card) {

    /*
       যদি একই card খোলা থাকে,
       তাহলে বন্ধ হবে।
    */

    const isActive =
        card.classList.contains("active");


    /*
       অন্য সব card বন্ধ করা
    */

    document
        .querySelectorAll(".info-card")
        .forEach(function (item) {

            item.classList.remove("active");

        });


    /*
       যেটাতে click করা হয়েছে
       সেটি যদি আগে বন্ধ থাকে,
       তাহলে খুলবে।
    */

    if (!isActive) {

        card.classList.add("active");

    }

}


/* ==========================================
   PAGE LOADED
========================================== */

document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log(
            "About the App page loaded successfully."
        );

    }
);