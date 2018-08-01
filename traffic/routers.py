class TrafficRouter(object):
    def db_for_read(self, model, **hints):
        "Point all operations on traffic models to 'trafficnow database'"
        if model._meta.db_table == 'trafficnow':
            return 'traffic'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on traffic models to 'trafficnow database'"
        if model._meta.db_table == 'trafficnow':
            return 'traffic'
        return 'default'
