Name:           ros-jade-posedetection-msgs
Version:        4.0.0
Release:        0%{?dist}
Summary:        ROS posedetection_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/posedetection_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-cv-bridge
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-message-filters
Requires:       ros-jade-message-runtime
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-message-filters
BuildRequires:  ros-jade-message-generation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs

%description
posedetection_msgs provides messages and services to facilitate passing pose
detection results and features.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Sep 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 4.0.0-0
- Autogenerated by Bloom

* Sat Jun 18 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 3.0.0-0
- Autogenerated by Bloom

* Sun Jan 24 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.1-0
- Autogenerated by Bloom

* Sun Jun 21 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 2.0.0-0
- Autogenerated by Bloom

