FROM colomoto/colomoto-docker:2020-08-01
MAINTAINER Vincent Noel <contact@vincent-noel.fr>

USER root

RUN apt-get -qq update && apt install -yq libgts-dev libgts-bin
RUN conda remove --force -y graphviz

RUN mkdir -p /notebook/IndividualTrajectoryAnalysis/
COPY . /notebook/IndividualTrajectoryAnalysis/

RUN chown -R user:user /notebook/IndividualTrajectoryAnalysis
USER user
