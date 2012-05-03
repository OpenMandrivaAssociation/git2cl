Summary: Converts git logs to GNU style ChangeLog format
Name: git2cl
Version: 2.0
Release: 0.0.git8373c9f
Group: Development/Other
License: GPLv2+
URL: http://josefsson.org/git2cl/
# Source is generated from a git tag. This
# shows an example of producing a tar ball from
# the  2.0 tag.
# git clone http://repo.or.cz/r/git2cl.git 
# cd git2cl
# git archive --prefix=git2cl-2.0/  git2cl-2.0 | gzip -c > git2cl-2.0.tar.gz
# And finally to get git hash for use in the release.
# git checkout git2cl-2.0
Source0: git2cl-2.0.tar.gz
BuildArch: noarch
Requires: git

%description
A quick tool to convert git logs to GNU ChangeLog format.

The tool invokes git log internally unless you pipe a log to it. 

%prep

%setup -q

%build
# Nothing to build.

%install
install -d %{buildroot}%{_bindir}
install -m0755 git2cl %{buildroot}%{_bindir}/git2cl

%files
%doc README COPYING
%{_bindir}/git2cl
