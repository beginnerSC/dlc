#ifndef DLC_CORE_VECTOR_H
#define DLC_CORE_VECTOR_H

#include <stdexcept>
#include <iostream>

class Vector {
 private:
  int* a_;
  size_t size_;
  size_t capacity_;

  // Helper method to allocate and initialize array
  int* GetInitializedArray(size_t capacity);

 public:
  // Constructors and destructors
  Vector();
  explicit Vector(int size);
  Vector(const Vector& other);
  Vector(Vector&& other);
  ~Vector();

  // Iterator class
  class Iterator {
    int* ptr_;

   public:
    explicit Iterator(int* ptr) noexcept;
    int& operator*() const noexcept;
    int* operator->() const noexcept;
    Iterator& operator++() noexcept;
    Iterator operator++(int) noexcept;
    bool operator==(Iterator other) const noexcept;
    bool operator!=(Iterator other) const noexcept;
  };

  // Iterator methods
  Iterator begin() const noexcept;
  Iterator end() const noexcept;

  // Public methods
  void Print();
  void PushBack(const int& val);
  void Resize(const size_t& size);
  size_t Size() const noexcept;

  // Assignment operators
  Vector& operator=(const Vector& other) noexcept;
  Vector& operator=(Vector&& other) noexcept;

  // Subscript operators
  int& operator[](size_t i) noexcept;
  const int& operator[](size_t i) const noexcept;
};

#endif