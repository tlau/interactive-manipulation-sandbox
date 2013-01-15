import roslib
import sys, os.path, inspect

class ActivityLoader:
    def __init__(self, packages):
        '''
        Finds and loads python classes which define activities.
        '''
        self._activity_classes = {}
        self._activity_goal_classes = {}

        # hardcoded to look in files in <package_name>/src for subclasses
        # of activity base
        for package_name in packages:
            package_dir = roslib.packages.get_pkg_dir(package_name)
            sys.path.append(os.path.join(package_dir, 'src'))
            module = __import__(package_name)
            
        # TODO hardcoded for the moment; should automatically find classes
        # based on ROS parameters


        # FIXME Uuuuuugly hack. pr2_activities depends on activity_manager, so activity_manager
        # can't depend on pr2_activities. Instead we manually find pr2_activities and add it to the python
        # path
        pr2_activities_dir = roslib.packages.get_pkg_dir('pr2_activities')
        sys.path.append(os.path.join(pr2_activities_dir, 'src'))
        from pr2_activities.dummy import Dummy
        activity_type = 'pr2_activities/dummy'
        self._activity_classes[activity_type] = Dummy
        from pr2_activities.msg import DummyActivityGoal
        self._activity_goal_classes[activity_type] = DummyActivityGoal

    def get_activity_class(self, activity_type):
        return self._activity_classes[activity_type]

    def get_activity_goal_class(self, activity_type):
        return self._activity_goal_classes[activity_type]

if __name__ == '__main__':
    al = ActivityLoader(['pr2_activities'])
