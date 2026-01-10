#include "dlc_core/vector.h"

int main() {
  size_t size = 3;
  Vector v(size);

  for (Vector::iterator it = v.begin(); it != v.end(); it++) {
    std::cout << *it << ", ";
  }
  std::cout << std::endl;

  for (const int& val : v) {
    std::cout << val << ", ";
  }
  std::cout << std::endl;

  for (int i = 0; i < 2 * size; ++i) {
    v.PushBack(i);
  }

  v.Print();

  std::cout << v[1] << ", " << v[7] << ", " << std::endl;

  v[3] = 10;
  v.Print();

  std::cout << "copy assignment: " << std::endl;
  Vector u;

  u = v;
  u[3] = 20;
  u.Print();

  std::cout << "copy ctor: " << std::endl;
  Vector x = v;
  x.Print();

  std::cout << "Resize: " << std::endl;
  v.Resize(20);
  v.Print();

  v.Resize(5);
  v.Print();

  v.Resize(40);
  v.Print();

  v.Resize(5);
  v.Print();

  std::cout << "move assignment: " << std::endl;
  v = std::move(x);
  v.Print();

  return 0;
}
