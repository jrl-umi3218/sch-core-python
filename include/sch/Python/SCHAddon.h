// This file is part of sch-core-python.
//
// sch-core-python is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published
// by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// sch-core-python is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with sch-core-python.  If not, see <http://www.gnu.org/licenses/>.

namespace sch
{

  void transform(S_Object& obj, const sva::PTransformd& t)
  {
    sch::Matrix4x4 m;
    const Eigen::Matrix3d& rot = t.rotation();
    const Eigen::Vector3d& tran = t.translation();

    for(int i = 0; i < 3; ++i)
    {
      for(int j = 0; j < 3; ++j)
      {
        m(i,j) = rot(j,i);
      }
    }

    m(0,3) = tran(0);
    m(1,3) = tran(1);
    m(2,3) = tran(2);

    obj.setTransformation(m);
  }


  S_Object* Sphere(double radius)
  {
    return new S_Sphere(radius);
  }


  S_Object* Box(double x, double y, double z)
  {
    return new S_Box(x, y, z);
  }


  S_Object* STPBV(const std::string& filename)
  {
    STP_BV* s = new STP_BV;
    s->constructFromFile(filename);
    return s;
  }


  S_Polyhedron* Polyhedron(const std::string& filename)
  {
    S_Polyhedron* s = new S_Polyhedron;
    s->constructFromFile(filename);
    return s;
  }

  double distance(CD_Pair& pair, Eigen::Vector3d& p1, Eigen::Vector3d& p2)
  {
    sch::Point3 p1Tmp, p2Tmp;
    double dist = pair.getClosestPoints(p1Tmp, p2Tmp);

    p1 << p1Tmp[0], p1Tmp[1], p1Tmp[2];
    p2 << p2Tmp[0], p2Tmp[1], p2Tmp[2];

    return dist;
  }

  std::vector<Eigen::Vector3d> vertices(S_Polyhedron& poly)
  {
    const Polyhedron_algorithms* pa = poly.getPolyhedronAlgorithm();
    std::vector<Eigen::Vector3d> vec;
    vec.reserve(pa->vertexes_.size());
    for(std::size_t i = 0; i < pa->triangles_.size(); ++i)
    {
      Vector3 normal = pa->triangles_[i].normal;
      vec.push_back(Eigen::Vector3d(normal[0], normal[1], normal[2]));
    }
    return vec;
  }

  std::vector<Eigen::Vector3d> normals(S_Polyhedron& poly)
  {
    const Polyhedron_algorithms* pa = poly.getPolyhedronAlgorithm();
    std::vector<Eigen::Vector3d> vec;
    vec.reserve(pa->triangles_.size());
    for(std::size_t i = 0; i < pa->vertexes_.size(); ++i)
    {
      Vector3 coordinates = pa->vertexes_[i]->getCordinates();
      vec.push_back(Eigen::Vector3d(coordinates[0], coordinates[1], coordinates[2]));
    }
    return vec;
  }

  std::vector<std::vector<unsigned int> > triangles(S_Polyhedron& poly)
  {
    const Polyhedron_algorithms* pa = poly.getPolyhedronAlgorithm();
    std::vector<std::vector<unsigned int>> vec;
    vec.reserve(pa->triangles_.size());
    for(std::size_t i = 0; i < pa->vertexes_.size(); ++i)
    {
      const PolyhedronTriangle triangle = pa->triangles_[i];
      std::vector<unsigned int> tri = {triangle.a, triangle.b, triangle.c};
      vec.push_back(tri);
    }
    return vec;
  }

}

