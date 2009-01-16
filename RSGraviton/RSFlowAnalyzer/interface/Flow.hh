#ifndef _flow_hh_included_
#define _flow_hh_included_
#include <vector>
#include "DataFormats/Math/interface/Vector3D.h"
#include "PhysicsTools/Utilities/interface/Parameter.h"
#include <boost/shared_ptr.hpp>
#include <cmath>
#include "Plane.hh"

// Class Flow to calculate the flow of Tracks inside a Jet.
struct Flow {

  typedef std::vector<math::XYZVector> VectorCollection;

  // Default constructor.
  Flow() {}

  // Constructor that takes one reference vector and one vector collection.
  // (In my use case, these are the jet and the tracks).
  // This is a rather convoluted constructor: we create the normal plane
  // with the reference vector and project every vector from the vector
  // collection in that plane.
  Flow(const math::XYZVector r, const VectorCollection& vc, const funct::Parameter& phi): 
    phiAngle(phi.ptr()), refPlane(r) {
    for(size_t i=0; i!=vc.size(); i++) {                                                                                                                           
      math::XYZVector thisProj = refPlane.projection2d(vc.at(i));
      projVectors.push_back(thisProj);
    }
  }
  
  // Function to calculate the flow given an angle Phi. 
  double operator()() const {
    double scalarFlow = 0.0;
    double denominator = 0.0;
    for(size_t i=0; i!=projVectors.size(); ++i) {
      scalarFlow += fabs( projVectors.at(i).X()*cos( *phiAngle) +
			  projVectors.at(i).Y()*sin( *phiAngle) );
      denominator += projVectors.at(i).R();
    }
    scalarFlow = scalarFlow/denominator;
    // We return minus the scalarFlow so we can minimize this function -> maximize the flow.
    return -scalarFlow;
  }

  // The members
  boost::shared_ptr<double> phiAngle;
  Plane refPlane;
  VectorCollection projVectors;
  
};
#endif
