import PyPDF2
import resume_scoring

# Function to fetch resume text from a PDF
def fetch_resume(pdf_file):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
        
        if not text:
            raise ValueError("No text extracted from PDF.")
        return text
    
    except Exception as e:
        print(f"Error parsing resume: {e}")
        return ""

# Function to parse resume for specific details
def parse_resume(resume_text):
    # Extract scoring and specified details
    details = {
        'scores': resume_scoring.calculate_resume_score(resume_text),
    }
    return details

# Function to take a file as input and return parsed scoring details and other required information
def extract_resume_details(pdf_file):
    resume_text = fetch_resume(pdf_file)
    return parse_resume(resume_text)
