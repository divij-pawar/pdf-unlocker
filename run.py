import PyPDF4

def decrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as file:
        reader = PyPDF4.PdfFileReader(file)
        
        if reader.isEncrypted:
            reader.decrypt(password)
            
        writer = PyPDF4.PdfFileWriter()
        
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            writer.addPage(page)
            
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

input_file = input("Enter input file: ")
output_file = input("Enter output file name: ")
password = input("Enter password: ")

decrypt_pdf(input_file, output_file, password)
print('Decryption completed successfully!')