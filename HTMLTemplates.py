html_sender = """
<style>
.chat-container {
    display: flex;
    flex-direction: column;
}

.sender-bubble {
    align-self: flex-start; /* Align user's message to the left */
    background-color: #007bff;
    color: white;
    padding: 12px 18px;
    border-radius: 18px 18px 0px 18px;
    max-width: 75%;
    font-size: 15px;
    line-height: 1.5;
    word-wrap: break-word;
    box-shadow: 0 1px 4px rgba(0,0,0,0.1);
    margin: 10px 0;
    font-family: 'Segoe UI', sans-serif;
    text-align: left;  /* Ensure text is left-aligned */
}
</style>
<div class="chat-container">
    <div class="sender-bubble">
        {{MESSAGE}}
    </div>
</div>
"""

html_bot = """
<style>
.chat-container {
    display: flex;
    flex-direction: column;
}

.receiver-bubble {
    align-self: flex-end; /* Align bot's message to the right */
    background-color: #e2e8f0;
    color: #1a202c;
    padding: 12px 18px;
    border-radius: 18px 18px 18px 0px;
    max-width: 75%;
    font-size: 15px;
    line-height: 1.5;
    word-wrap: break-word;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    margin: 10px 0;
    font-family: 'Segoe UI', sans-serif;
    text-align: left;  /* Ensure text is left-aligned */
}
</style>
<div class="chat-container">
    <div class="receiver-bubble">
        {{MESSAGE}}
    </div>
</div>
"""
