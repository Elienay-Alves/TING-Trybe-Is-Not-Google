def exists_word(word, instance):
    result = list()

    for data in instance.items:
        lines = data["linhas_do_arquivo"]
        file_name = data["nome_do_arquivo"]
        result.append(
            {
                "arquivo": file_name,
                "ocorrencias": [
                    {"linha": index + 1}
                    for index, line in enumerate(lines)
                    if word.lower() in line.lower()
                ],
                "palavra": word.lower(),
            }
        )
    if not result[0]["ocorrencias"]:
        return []
    return result


def search_by_word(word, instance):
    result = []
    for file_index in range(len(instance)):
        data = instance.search(file_index)
        lines = data["linhas_do_arquivo"]
        file_name = data["nome_do_arquivo"]
        occurrences = [
            {"linha": index + 1, "conteudo": line}
            for index, line in enumerate(lines)
            if word.lower() in line.lower()
        ]
        if len(occurrences):
            result.append(
                {
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                    "palavra": word,
                }
            )
    return result
