# Infinsa Bot  

## About The Project 

**Infinsa Bot Backend** is the server-side implementation for the Infinsa Bot app. It is designed to handle chat interactions, voice input, and financial data processing for elder-friendly financial assistance. The backend integrates advanced AI capabilities to provide personalized and user-friendly financial insights.

### **Features**  

- **Chat and Voice Interaction**: Handles chat and voice-based user queries with dedicated endpoints.  
- **Prompts for Financial Categories**: Custom prompts for various financial categories, including accounts, loans, investments, and more.  
- **Security Email Service**: Sends automated security alerts and notifications.  
- **Built with Haystack**: Uses Haystack framework for efficient retrieval-augmented generation (RAG) and search capabilities.  
- **Powered by Gemini LLMs**: Leverages the latest advancements in language models to ensure high accuracy and contextual understanding.

### **Built With**  

- **Python**: Backend programming language.  
- **Haystack Framework**: Open-source framework for building LLM applications, retrieval-augmented generation pipelines, and advanced search systems.  
- **Gemini LLMs**: High-performance large language models tailored for financial data comprehension and natural language processing.  

## **Getting Started**  

1. **Clone the Repository**  
   Clone the backend repository to your local machine.  
   ```bash
   git clone https://github.com/MettaSurendhar/Infinsa-App-server.git
   ```

2. **Install Dependencies**  
   Set up the required Python packages.  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**  
   Start the backend server using the following command:  
   ```bash
   uvicorn app:app --reload
   ```

4. **Connect with Frontend**  
   Publish the backend and connect it to the Infinsa Bot app frontend.

## **Usage**  

Infinsa Bot is available in multiple formats:  
1. **Web Application**: Access the published web app here: [Infinsa Bot Web App](https://infinsa-bot-app.flutterflow.app/).  
2. **Mobile Application**: Download the APK from [apk download](https://github.com/MettaSurendhar/Infinsa-App/releases/download/v0.1.0-alpha/Infinsa.App-release.apk).


### **API Routes**  

1. **Chat Interaction**  
   - Endpoint: `/api/chat`  
   - Handles user queries with structured financial data inputs.  
   - Example: Provides account summaries or budget recommendations.  

2. **Voice Interaction**  
   - Endpoint: `/app/chat/voice`  
   - Accepts voice files and processes queries for financial assistance.  

3. **Voice-to-Text Conversion**  
   - Endpoint: `/voice`  
   - Converts uploaded voice files into actionable queries using AI-based transcription.  

### **Agents**  

- **Agent**: Manages overall query processing.  
- **Chat Agent**: Specializes in text-based chat responses.  
- **Voice Agent**: Handles voice input and processing.  


### **Prompt Categories**  

The backend uses a rich set of prompts customized for elder users across multiple financial categories:  

- **Account Assistance**: Simplified account summaries.  
- **Credit Card Help**: Clear explanations of credit card details.  
- **Loan Information**: Easy-to-understand loan overviews.  
- **Investment Guidance**: Insights into investments and returns.  
- **Transaction Summaries**: Details of recent transactions.  
- **Budget Planning**: Personalized financial advice for budgets.  
- **Expense Tracking**: Overview of categorized spending.  
- **Savings Tracking**: Tips and progress on savings goals.  
- **Financial Health**: Insights into overall financial health and recommendations.

## Contributing  
Contributions make the open-source community an inspiring and creative space. We welcome all contributions!  

To contribute:  
1. Fork the Project.  
2. Create your Feature Branch:  
   ```bash  
   git checkout -b feature/AmazingFeature  
   ```  
3. Commit your Changes:  
   ```bash  
   git commit -m "Add some AmazingFeature"  
   ```  
4. Push to the Branch:  
   ```bash  
   git push origin feature/AmazingFeature  
   ```  
5. Open a Pull Request.  

## License  
Distributed under the MIT License. See `LICENSE` for more information. 
