




from seasons import birthday


def main() :
  test_function()


def test_function() :

  assert birthday("1998-10-10") == ("1998", "10", "10")

  assert birthday("1991-07-02") == ("1991", "07", "02")


  assert birthday("1992-4-1") == None


if __name__ == "__main__":
  main()

