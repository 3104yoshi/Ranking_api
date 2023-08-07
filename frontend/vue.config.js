const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  outputDir: '../dist/',
  assetsDir: 'static',
  devServer: {
    proxy: 'http://localhost:5000'
  },
  transpileDependencies: true,
  configureWebpack: {
    devtool: 'source-map'
  }
})
