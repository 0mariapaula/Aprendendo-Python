def  notas (*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = {}
    r['total'] = len(n)
    r['maior'] = max(n) if n else 0
    r['menor'] = min(n) if n else 0
    r['media'] = sum(n) / len(n) if n else 0
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'Aprovado'
        elif r['media'] >= 5:
            r['situacao'] = 'Recuperação'
        else:
            r['situacao'] = 'Reprovado'
    return r