from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    if path_file not in [item["nome_do_arquivo"] for item in instance.items]:
        file = txt_importer(path_file)
        data = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }

        instance.enqueue(data)
        print(data, file=sys.stdout)


def remove(instance):
    if not len(instance):
        return print("Não há elementos")
    file = instance.dequeue()
    print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(f"{instance.search(position)}")
    except IndexError:
        print("Posição inválida", file=sys.stderr)
