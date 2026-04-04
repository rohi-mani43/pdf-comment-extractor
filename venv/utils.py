import fitz

def extract_pdf_comments(file_stream):
    doc = fitz.open(stream=file_stream, filetype="pdf")
    comments = []

    for page_num, page in enumerate(doc, start=1):
        annotations = page.annots()

        if annotations:
            for annot in annotations:
                content = annot.info.get("content", "")

                if content.strip() and len(content.strip()) > 5:
                    comments.append({
                        "page": page_num,
                        "comment": content.strip()
                    })

    return comments