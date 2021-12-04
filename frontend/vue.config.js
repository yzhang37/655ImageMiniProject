module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8088',
                ws: true,
                changeOrigin: true
            },
            '/img/': {
                target: 'http://localhost:8088',
                ws: true,
                changeOrigin: true
            },
        }
    }
}