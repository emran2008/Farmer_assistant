/* ==========================================
   USER GUIDE
========================================== */

function toggleGuide(card) {

    const isActive =
        card.classList.contains("active");


    /*
       সব card বন্ধ করা
    */

    document
        .querySelectorAll(".guide-card")
        .forEach(function (item) {

            item.classList.remove("active");

        });


    /*
       যেটাতে click করা হয়েছে
       সেটি খুলবে
    */

    if (!isActive) {

        card.classList.add("active");

    }

}