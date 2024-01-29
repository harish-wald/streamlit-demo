# # Importing the os module to perform file operations
# import os  
# # Importing the pytesseract module to extract text from images
# import pytesseract as tess  
# # Importing the Image module from the PIL package to work with images
# from PIL import Image  
# # Importing the convert_from_path function from the pdf2image module to convert PDF files to images
# from pdf2image import convert_from_path  

# #This function takes a PDF file name as input and returns the name of the text file that contains the extracted text.
# def read_pdf(file_name):   
#     # Store all pages of one file here:
#     pages = []

#     try:
#         # Convert the PDF file to a list of PIL images:
#         images = convert_from_path(file_name)  

#         # Extract text from each image:
#         for i, image in enumerate(images):
#           # Generating filename for each image
#             filename = "page_" + str(i) + "_" + os.path.basename(file_name) + ".jpeg"  
#             image.save(filename, "JPEG")  
#           # Saving each image as JPEG
#             text = tess.image_to_string(Image.open(filename))  # Extracting text from each image using pytesseract
#             pages.append(text)  
#           # Appending extracted text to pages list

#     except Exception as e:
#         print(str(e))

#     # Write the extracted text to a file:
#     output_file_name = os.path.splitext(file_name)[0] + ".txt"  # Generating output file name
#     with open(output_file_name, "w") as f:
#         f.write("\n".join(pages))  
#       # Writing extracted text to output file

#     return output_file_name

# #print function returns the final converted text 
# pdf_file = "MMM Bye-Laws.pdf"
# print(read_pdf(pdf_file))


from pathlib import Path
from llama_index import download_loader, VectorStoreIndex
import os 

openai.api_key = st.secrets["OPENAI_API_KEY"]

PDFReader = download_loader("PDFReader")

loader = PDFReader()

documents = loader.load_data(file=Path('MMM Bye-Laws (1) (1).pdf'))

print(documents)

index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

st.title('Magna Majestic Meadows ByLaws GPT')

query = st.text_area('Query', 'Enter your query')

def run_prompt():
    st.subheader('Output: ')
    st.write(query_engine.query(query))

st.button('Run', on_click=run_prompt)