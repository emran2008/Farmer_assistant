// =====================================
// FARMER ASSISTANT JAVASCRIPT
// =====================================

// Navigation items select
const navItems = document.querySelectorAll(".nav-item");

// Navigation click event
navItems.forEach(function(item) {

    item.addEventListener("click", function() {

        console.log(
            "Navigation clicked:",
            item.innerText
        );

    });

});


// =====================================
// CROP RECOMMENDATION CARD
// =====================================

const cropCard = document.querySelector(".crop-card");

if (cropCard) {

    cropCard.addEventListener("click", function() {

        console.log("Crop Recommendation clicked!");

    });

}
/* =========================================
   MORE SCREEN
========================================= */

function openMore() {

    const moreScreen = document.getElementById("moreScreen");

    moreScreen.style.display = "block";

}


function closeMore() {

    const moreScreen = document.getElementById("moreScreen");

    moreScreen.style.display = "none";

}

