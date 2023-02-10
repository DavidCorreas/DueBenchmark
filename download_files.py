import os
import requests

docvqa = "https://applica-public.s3.eu-west-1.amazonaws.com/due/datasets/DocVQA.tar.gz"
infographicsvqa = "https://applica-public.s3.eu-west-1.amazonaws.com/due/datasets/InfographicsVQA.tar.gz"
kleistercharity = "https://applica-public.s3.eu-west-1.amazonaws.com/due/datasets/KleisterCharity.tar.gz"
wtq = "https://applica-public.s3.eu-west-1.amazonaws.com/due/datasets/WikiTableQuestions.tar.gz"
pwc = "https://applica-public.s3.eu-west-1.amazonaws.com/due/datasets/PWC.tar.gz"
deepform = "https://applica-public.s3.eu-west-1.amazonaws.com/due/datasets/DeepForm.tar.gz"
tabfact = "https://applica-public.s3.eu-west-1.amazonaws.com/due/datasets/TabFact.tar.gz"

docvqa_pdf = "https://applica-public.s3.eu-west-1.amazonaws.com/due/pdfs/DocVQA.tar.gz"
infographicsvqa_pdf = "https://applica-public.s3.eu-west-1.amazonaws.com/due/pdfs/InfographicsVQA.tar.gz"
kleistercharity_pdf = "https://applica-public.s3.eu-west-1.amazonaws.com/due/pdfs/KleisterCharity.tar.gz"
wtq_pdf = "https://applica-public.s3.eu-west-1.amazonaws.com/due/pdfs/WikiTableQuestions.tar.gz"
pwc_pdf = "https://applica-public.s3.eu-west-1.amazonaws.com/due/pdfs/PWC.tar.gz"
deepform_pdf = "https://applica-public.s3.eu-west-1.amazonaws.com/due/pdfs/DeepForm.tar.gz"
tabfact_pdf = "https://applica-public.s3.eu-west-1.amazonaws.com/due/pdfs/TabFact.tar.gz"

json_datasets = [docvqa, infographicsvqa, kleistercharity, wtq, pwc, deepform, tabfact]
pdf_datasets = [docvqa_pdf, infographicsvqa_pdf, kleistercharity_pdf, wtq_pdf, pwc_pdf, deepform_pdf, tabfact_pdf]
download_json_path = "/workspaces/udop/due-benchmark/raw_data/json"
download_pdf_path = "/workspaces/udop/due-benchmark/raw_data/pdf"

# Download every dataset
for dataset in json_datasets:
    print("Downloading dataset: {}".format(dataset))
    r = requests.get(dataset, allow_redirects=True)
    basename = os.path.basename(dataset)
    open(os.path.join(download_json_path, basename), 'wb').write(r.content)
    
# Download every dataset
for dataset in pdf_datasets:
    print("Downloading dataset: {}".format(dataset))
    r = requests.get(dataset, allow_redirects=True)
    basename = os.path.basename(dataset)
    open(os.path.join(download_pdf_path, basename), 'wb').write(r.content)

# Unzip every dataset
for dataset in json_datasets:
    basename = os.path.basename(dataset)
    os.system("tar -xzf {} -C {}".format(os.path.join(download_json_path, basename), download_json_path))

# Unzip every dataset
for dataset in pdf_datasets:
    basename = os.path.basename(dataset)
    os.system("tar -xzf {} -C {}".format(os.path.join(download_pdf_path, basename), download_pdf_path))
    