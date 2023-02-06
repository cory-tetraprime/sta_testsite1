'use strict';

/**
 * article-status service
 */

const { createCoreService } = require('@strapi/strapi').factories;

module.exports = createCoreService('api::article-status.article-status');
