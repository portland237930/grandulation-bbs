import request from './request'
export const reqUserRegister = (data) =>
  request({
    url: '/user/user',
    methods: 'POST',
    // headers: { 'content-type': 'application/x-www-form-urlencoded' },
    data,
  })
