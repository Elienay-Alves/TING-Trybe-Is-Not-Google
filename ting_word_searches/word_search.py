def exists_word(word, instance):
    result = list()

    for data in instance.items:
        lines = "linhas_do_arquivo"
        file_name = "nome_do_arquivo"
        result.append(
            {
                "arquivo": data[file_name],
                "ocorrencias": [
                    {"linha": index + 1}
                    for index, line in enumerate(data[lines])
                    if word.lower() in line.lower()
                ],
                "palavra": word.lower(),
            }
        )
    if not result[0]["ocorrencias"]:
        return []
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
