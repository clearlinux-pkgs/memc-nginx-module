#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : memc-nginx-module
Version  : 0.19
Release  : 12
URL      : https://github.com/openresty/memc-nginx-module/archive/v0.19.tar.gz
Source0  : https://github.com/openresty/memc-nginx-module/archive/v0.19.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: memc-nginx-module-lib = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev

%description
Name
====
**ngx_memc** - An extended version of the standard memcached module that supports set, add, delete, and many more memcached commands.

%package lib
Summary: lib components for the memc-nginx-module package.
Group: Libraries

%description lib
lib components for the memc-nginx-module package.


%prep
%setup -q -n memc-nginx-module-0.19
cd %{_builddir}/memc-nginx-module-0.19

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
nginx-module install %{buildroot}


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_memc_module.so
