import itertools

def bw_encode(data):
  """
  Прямое преобразование Барроуза-Уиллера
  :@param data: кодируемая строка
  """
  return "".join(list(map(lambda permut : permut[len(data) - 1],
              sorted([(data[i:] + data[:i]) for i in range(len(data))]))))


def bw_decode(data):
  """
  Обратное преобразование Барроуза-Уиллера
  :@param data: закодированная строка
  """
  N = len(data)
  table = ["" for i in range(N)]

  for i in range(N):
    for j in range(N):
      table[j] = data[j] + table[j]
    table.sort()

  for word in table:
    if word[-1] == "\n":
      return word
  return None


def rle_encode(data):
  """
  RLE-сжатие
  :@param data: кодируемые данные
  """
  return [(k, len(list(g))) for k, g in itertools.groupby(data)]


def main():
  """
  Точка входа
  """
  string = "BANANA\n"

  bw_encoded = bw_encode(string)
  bw_decoded = bw_decode(bw_encoded)
  rle_encoded = rle_encode(string)

  print(f"Закодированные строки: {bw_encoded}, {rle_encoded}")
  print(f"Декодированная строка: {bw_decoded}")


if __name__ == "__main__":
  main()
