
import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
Chatbot.init({
        chatflowid: "c980cb30-f2c9-4234-934e-0047f7d187d2",
        apiHost: "https://flowise-94ny.onrender.com",
        chatflowConfig: {
            // topK: 2
        },
        theme: {
            button: {
                backgroundColor: "#184A78",
                right: 30,
                bottom: 30,
                size: 58, // small | medium | large | number
                dragAndDrop: true,
                iconColor: "white",
                customIconSrc: "../static/messenger.png",
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
                title: 'Luis Assistant',
                titleAvatarSrc: '../static/messenger.png',
                showAgentMessages: true,
                welcomeMessage: 'Hello! How can I help you?',
                errorMessage: 'This is a custom error message',
                backgroundColor: "#ffffff",
                backgroundImage: 'enter image path or link', // If set, this will overlap the background color of the chat window.
                height: 600,
                width: 400,
                fontSize: 16,
                //starterPrompts: ['What is a bot?', 'Who are you?'], // It overrides the starter prompts set by the chat flow passed
                starterPromptFontSize: 15,
                clearChatOnReload: false, // If set to true, the chat will be cleared when the page reloads.
                botMessage: {
                    backgroundColor: "#f7f8ff",
                    textColor: "#303235",
                    showAvatar: true,
                    avatarSrc: "../static/profile.jpg",
                },
                userMessage: {
                    backgroundColor: "#3B81F6",
                    textColor: "#ffffff",
                    showAvatar: true,
                    avatarSrc: "../static/prm.png",
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
                footer: {
                    textColor: '#303235',
                    text: 'Powered by',
                    company: 'Luis Bello',
                    companyLink:'https://www.linkedin.com/in/luis-ernesto-p%C3%A9rez-bello/',
                }
            }
        }
})
