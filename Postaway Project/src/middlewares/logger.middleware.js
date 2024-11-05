import fs from 'fs';
import winston, { transports } from 'winston';
const fsPromise = fs.promises;

const logger = winston.createLogger({
    level: 'info',
    format: winston.format.json(),
    transports: [
        new winston.transports.File({filename: "logs.log"})
    ]
});

const loggerMiddleware = async (req, res, next) => {
    if(!req.url.includes("login") || !req.url.includes("signup")){
        const logData = `Date: ${new Date().toLocaleString()}, URL: ${req.url}, - Data: ${JSON.stringify(req.body)}`
        logger.info(logData);   
    }
    next();
}

export default loggerMiddleware;