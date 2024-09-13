
    import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
    Chatbot.init({
        chatflowid: "c980cb30-f2c9-4234-934e-0047f7d187d2",
        apiHost: "https://flowise-94ny.onrender.com",
        chatflowConfig: {
            // topK: 2
        },
        theme: {
            button: {
                backgroundColor: "#3B81F6",
                right: 20,
                bottom: 20,
                size: 48, // small | medium | large | number
                dragAndDrop: true,
                iconColor: "white",
                customIconSrc: "https://raw.githubusercontent.com/walkxcode/dashboard-icons/main/svg/google-messages.svg",
                autoWindowOpen: {
                    autoOpen: true, //parameter to control automatic window opening
                    openDelay: 2, // Optional parameter for delay time in seconds
                    autoOpenOnMobile: false, //parameter to control automatic window opening in mobile
                    },
            },
            tooltip: {
                showTooltip: true,
                tooltipMessage: 'Hi👋!',
                tooltipBackgroundColor: 'black',
                tooltipTextColor: 'white',
                tooltipFontSize: 16,
            },
            chatWindow: {
                showTitle: true,
                title: 'Luis Bot',
                titleAvatarSrc: 'https://raw.githubusercontent.com/walkxcode/dashboard-icons/main/svg/google-messages.svg',
                showAgentMessages: true,
                welcomeMessage: 'Hello! ',
                errorMessage: 'This is a custom error message',
                backgroundColor: "#ffffff",
                backgroundImage: 'enter image path or link', // If set, this will overlap the background color of the chat window.
                height: 700,
                width: 400,
                fontSize: 16,
                //starterPrompts: ['What is a bot?', 'Who are you?'], // It overrides the starter prompts set by the chat flow passed
                starterPromptFontSize: 15,
                clearChatOnReload: false, // If set to true, the chat will be cleared when the page reloads.
                botMessage: {
                    backgroundColor: "#f7f8ff",
                    textColor: "#303235",
                    showAvatar: true,
                    avatarSrc: "",
                },
                userMessage: {
                    backgroundColor: "#3B81F6",
                    textColor: "#ffffff",
                    showAvatar: true,
                    avatarSrc: "",
                },
                textInput: {
                    placeholder: 'Type your question',
                    backgroundColor: '#ffffff',
                    textColor: '#303235',
                    sendButtonColor: '#3B81F6',
                    maxChars: 50,
                    maxCharsWarningMessage: 'You exceeded the characters limit. Please input less than 50 characters.',
                    autoFocus: true, // If not used, autofocus is disabled on mobile and enabled on desktop. true enables it on both, false disables it on both.
                    sendMessageSound: true,
                    // sendSoundLocation: "send_message.mp3", // If this is not used, the default sound effect will be played if sendSoundMessage is true.
                    receiveMessageSound: true,
                    // receiveSoundLocation: "receive_message.mp3", // If this is not used, the default sound effect will be played if receiveSoundMessage is true. 
                },
                feedback: {
                    color: '#303235',
                },
                
            }
        }
    })
