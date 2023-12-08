import os
import PyPDF2


def merge_pdfs_in_directory(input_dir, output_pdf):
    """
    Merge all PDF files in a directory into a single output PDF.

    Args:
    input_dir (str): The directory containing PDF files to merge.
    output_pdf (str): The output PDF file path.

    Returns:
    None.
    """
    try:
        # Check if the input directory exists
        if not os.path.isdir(input_dir):
            raise ValueError(f"The directory {input_dir} does not exist.")

        # Get all PDF files in the target directory
        pdf_files = [os.path.join(input_dir, filename) for filename in os.listdir(input_dir) if filename.lower().endswith('.pdf')]
        pdf_files.sort()  # Sort the files

        if not pdf_files:
            print("No PDF files found in the directory.")
            return

        # Use with statement to ensure proper resource management
        with PyPDF2.PdfMerger() as pdf_merger:
            # Merge each PDF file
            for pdf_file in pdf_files:
                pdf_merger.append(pdf_file)
            
            # Write the merged PDF file
            with open(output_pdf, 'wb') as output_file:
                pdf_merger.write(output_file)
        
        print(f'Successfully merged {len(pdf_files)} PDF files into {output_pdf}')
    except Exception as e:
        print(f'Error merging PDF files: {str(e)}')


if __name__ == "__main__":
    # input_directory = './pdf/studying-and-training-visas'  # Directory containing PDF files
    # output_pdf = './pdf/studying-and-training-visas.pdf'  # Path for the output merged PDF file

    # input_directory = './pdf/visitor-visas'  # Directory containing PDF files
    # output_pdf = './pdf/visitor-visas.pdf'  # Path for the output merged PDF file

    # input_directory = './pdf/working-and-skilled-visas'  # Directory containing PDF files
    # output_pdf = './pdf/working-and-skilled-visas.pdf'  # Path for the output merged PDF file

    input_directory = './pdf/au-visas'  # Directory containing PDF files
    output_pdf = './pdf/au-visas.pdf'  # Path for the output merged PDF file

    merge_pdfs_in_directory(input_directory, output_pdf)
