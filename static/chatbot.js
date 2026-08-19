async function sendMessage() {

    const input = document.getElementById("chat-input");
    const chatBox = document.getElementById("chat-box");

    if (!input || !chatBox) {
        console.error("Chat input বা chat box পাওয়া যাচ্ছে না!");
        return;
    }

    const message = input.value.trim();

    if (!message) {
        return;
    }

    // User message দেখানো
    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.textContent = message;

    chatBox.appendChild(userMessage);

    input.value = "";


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


       
    // =====================================================
    // BOT MESSAGE
    // =====================================================

    const botMessage = document.createElement("div");

    botMessage.className = "bot-message";

    botMessage.textContent =
        data.reply || "কোনো উত্তর পাওয়া যায়নি।";

    chatBox.appendChild(botMessage);

    console.log("CHATBOT DATA:", data);
    console.log("CHATBOT LINK:", data.link);
    // =====================================================
    // FEATURE LINK BUTTON
    // =====================================================

        if (data.link) {

            const featureButton = document.createElement("button");

            featureButton.className = "chat-feature-button";

            featureButton.textContent =
                data.link_text || "আরও তথ্য দেখুন";

            featureButton.addEventListener("click", function () {
                window.location.href = data.link;
            });

            chatBox.appendChild(featureButton);
        }

        chatBox.scrollTop = chatBox.scrollHeight;


    } catch (error) {

        console.error("Chatbot Error:", error);

        const errorMessage = document.createElement("div");
        errorMessage.className = "bot-message";
        errorMessage.textContent =
            "দুঃখিত, সার্ভারের সাথে যোগাযোগ করা যাচ্ছে না।";

        chatBox.appendChild(errorMessage);
    }
}


function handleKey(event) {

    if (event.key === "Enter") {
        sendMessage();
    }

}