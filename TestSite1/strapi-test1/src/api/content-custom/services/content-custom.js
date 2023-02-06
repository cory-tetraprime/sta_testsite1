'use strict';

/**
 * content-custom service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::content-custom.content-custom');
