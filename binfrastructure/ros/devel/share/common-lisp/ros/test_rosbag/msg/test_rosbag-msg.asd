
(cl:in-package :asdf)

(defsystem "test_rosbag-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Unmigrated" :depends-on ("_package_Unmigrated"))
    (:file "_package_Unmigrated" :depends-on ("_package"))
    (:file "Renamed4" :depends-on ("_package_Renamed4"))
    (:file "_package_Renamed4" :depends-on ("_package"))
    (:file "Converged" :depends-on ("_package_Converged"))
    (:file "_package_Converged" :depends-on ("_package"))
    (:file "SubUnmigrated" :depends-on ("_package_SubUnmigrated"))
    (:file "_package_SubUnmigrated" :depends-on ("_package"))
    (:file "MigratedMixed" :depends-on ("_package_MigratedMixed"))
    (:file "_package_MigratedMixed" :depends-on ("_package"))
    (:file "Constants" :depends-on ("_package_Constants"))
    (:file "_package_Constants" :depends-on ("_package"))
    (:file "MigratedImplicit" :depends-on ("_package_MigratedImplicit"))
    (:file "_package_MigratedImplicit" :depends-on ("_package"))
    (:file "MigratedExplicit" :depends-on ("_package_MigratedExplicit"))
    (:file "_package_MigratedExplicit" :depends-on ("_package"))
    (:file "SimpleMigrated" :depends-on ("_package_SimpleMigrated"))
    (:file "_package_SimpleMigrated" :depends-on ("_package"))
    (:file "MigratedAddSub" :depends-on ("_package_MigratedAddSub"))
    (:file "_package_MigratedAddSub" :depends-on ("_package"))
    (:file "PartiallyMigrated" :depends-on ("_package_PartiallyMigrated"))
    (:file "_package_PartiallyMigrated" :depends-on ("_package"))
    (:file "Simple" :depends-on ("_package_Simple"))
    (:file "_package_Simple" :depends-on ("_package"))
  ))