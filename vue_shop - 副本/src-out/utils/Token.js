// 设置令牌
export const setToken = (token) => {
  localStorage.setItem('TOKEN', token)
}
// 获得令牌
export const getToken = () => {
  return localStorage.getItem('TOKEN')
}
// 移除令牌
export const removeToken = () => {
  localStorage.removeItem('TOKEN')
}
// 创建uid
export const getUid = () => {
  return localStorage.getItem('uid')
}
// 创建uid
export const setUid = (uid) => {
  return localStorage.setItem('uid', uid)
}
// 移除uid
export const removeUid = () => {
  localStorage.removeItem('uid')
}
