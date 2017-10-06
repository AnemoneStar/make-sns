const webpack = require("webpack")

module.exports = {
    entry: "./client/index.js",
    output: {
        path: __dirname+"/dist",
        filename: "bundle.js",
        publicPath: "/assets/"
    },
    plugins: [
        new webpack.ProvidePlugin({
            riot: "riot",
            apiCall: __dirname+"/src/client/api-call.js"
        }),
        // new webpack.optimize.UglifyJsPlugin()
    ],
    module: {
        loaders: [
            { test: /\.tag$/, exclude: /node_modules/, loader: 'riot-tag-loader', query: {
                type: "none",
                template: "pug",
                style: "less"
            }},
            /*
            { test: /\.css$/, loader: 'style-loader!css-loader' },
            { test: /\.svg$/, loader: 'file-loader?mimetype=image/svg+xml' },
            { test: /\.woff$/, loader: 'file-loader?mimetype=application/font-woff' },
            { test: /\.woff2$/, loader: 'file-loader?mimetype=application/font-woff2' },
            { test: /\.eot$/, loader: 'file-loader?mimetype=application/vnd.ms-fontobject' },
            { test: /\.ttf$/, loader: 'file-loader?mimetype=font/truetype' }
            */
        ]
    }
}