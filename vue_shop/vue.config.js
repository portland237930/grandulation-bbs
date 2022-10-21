module.exports = {
    devServer: {
        proxy: {
            '/': {
                target: 'http://localhost:5000',
                changeOrigin: true,
                pathRewrite: {
                    '^/': ''
                }
            }
        }
    },
    // 配置根目录
    // publicPath: '/dist'
}