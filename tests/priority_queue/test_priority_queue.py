from ting_file_management.priority_queue import PriorityQueue
import pytest

data = [
    {
        "nome_do_arquivo": "name.txt",
        "qtd_linhas": 1,
        "linhas_do_arquivo": ["Lorem ipsum"],
    },
    {
        "nome_do_arquivo": "name.txt",
        "qtd_linhas": 23,
        "linhas_do_arquivo": ["Lorem ipsum"],
    },
]


def test_basic_priority_queueing():
    queue = PriorityQueue()

    queue.enqueue(data[0])
    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 0

    queue.enqueue(data[1])
    assert len(queue.regular_priority) == 1
    assert len(queue.high_priority) == 1

    assert queue.search(1) == data[1]

    queue.dequeue()
    assert queue.dequeue() is not None
    assert len(queue.high_priority) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(3)
