module.exports = {
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:8088',
                ws: false,
                changeOrigin: true
            },
            '/img/': {
                target: 'http://localhost:8088',
                ws: false,
                changeOrigin: true
            },
            '/': {
                target: 'ws://localhost:8088',
                ws: true,
                changeOrigin: true
            },
        }
    }
}