console.log("CHATBOT JS LOADED");


async function sendMessage() {

    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chatBox");

    if (!input || !chatBox) {
        console.error("Chat input বা chat box পাওয়া যাচ্ছে না!");
        return;
    }

    const message = input.value.trim();

    if (!message) {
        return;
    }


    // =========================================
    // USER MESSAGE
    // =========================================

    const userMessage = document.createElement("div");

    userMessage.className = "user-message";
    userMessage.textContent = message;

    chatBox.appendChild(userMessage);

    input.value = "";


    // =========================================
    // SEND TO FLASK
    // =========================================

    try {

        const response = await fetch("/api/chatbot", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        if (!response.ok) {
            throw new Error("HTTP error: " + response.status);
        }


        const data = await response.json();

        console.log("CHATBOT DATA:", data);
        console.log("CHATBOT LINK:", data.link);
        console.log("CHATBOT LINK TEXT:", data.link_text);


        // =========================================
        // BOT MESSAGE
        // =========================================

        const botMessage = document.createElement("div");

        botMessage.className = "bot-message";

        botMessage.textContent =
            data.reply || "কোনো উত্তর পাওয়া যায়নি।";

        chatBox.appendChild(botMessage);


        // =========================================
        // FEATURE LINK BUTTON
        // =========================================

        if (data.link) {

            const featureButton =
                document.createElement("button");

            featureButton.className =
                "chat-feature-button";

            featureButton.textContent =
                data.link_text || "আরও তথ্য দেখুন";


            featureButton.addEventListener("click", function () {

                console.log("FEATURE BUTTON CLICKED");
                console.log("Going to:", data.link);

                window.location.href = data.link;

            });


            chatBox.appendChild(featureButton);
        }


        // =========================================
        // AUTO SCROLL
        // =========================================

        chatBox.scrollTop = chatBox.scrollHeight;


    } catch (error) {

        console.error("Chatbot Error:", error);


        const errorMessage =
            document.createElement("div");

        errorMessage.className = "bot-message";

        errorMessage.textContent =
            "দুঃখিত, সার্ভারের সাথে যোগাযোগ করা যাচ্ছে না।";

        chatBox.appendChild(errorMessage);

        chatBox.scrollTop = chatBox.scrollHeight;

    }

}



// =========================================
// PAGE LOAD
// =========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("CHATBOT JS READY");


    const sendButton =
        document.getElementById("send-button");

    const chatInput =
        document.getElementById("chat-input");


    console.log("Send button:", sendButton);
    console.log("Chat input:", chatInput);


    // =========================================
    // SEND BUTTON
    // =========================================

    if (sendButton) {

        sendButton.addEventListener("click", function () {

            sendMessage();

        });

    } else {

        console.error("send-button পাওয়া যায়নি!");

    }


    // =========================================
    // ENTER KEY
    // =========================================

    if (chatInput) {

        chatInput.addEventListener("keydown", function (event) {

            if (event.key === "Enter") {

                event.preventDefault();

                sendMessage();

            }

        });

    } else {

        console.error("chat-input পাওয়া যায়নি!");

    }

});