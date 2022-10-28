// 字段比较函数
export const sortBy = (filed1, filed2) => {
  return function (a, b) {
    if (a.field1 == b.field1) return a.field2 - b.field2
    return a.field1 - b.field1
  }
}
