#include "Rivet/Analysis.hh"
#include "Rivet/Projections/MissingMomentum.hh"
#include "Rivet/AnalysisLoader.hh"

namespace Rivet {
  
  class StopThreeBody : public Analysis {  
  public:
    StopThreeBody() : Analysis("StopThreeBody") { }    
    
    void init() { 
      const FinalState cnfs;
      addProjection(MissingMomentum(cnfs), "ETmiss");
      _histMET    = bookHisto1D("MET", 100, 0, 3000);
    }
    
    void analyze(const Event& event) {
      const double weight = event.weight();
      const MissingMomentum& met = applyProjection<MissingMomentum>(event, "ETmiss");
      _histMET->fill(met.scalarEt(),weight);
    }
    
    void finalize(){
      MSG_DEBUG("Finalize");			
      scale(_histMET, 1/sumOfWeights());
    }

  private:
    Histo1DPtr _histMET;
  };

  DECLARE_RIVET_PLUGIN(StopThreeBody);
}